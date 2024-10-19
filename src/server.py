import json
import websocket  # NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import urllib.request
from requests_toolbelt import MultipartEncoder
import urllib.parse
import random
import os
import io
from PIL import Image


def open_websocket_connection(comfy_server_address):
    server_address = comfy_server_address
    client_id = str(uuid.uuid4())
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    return ws, server_address, client_id


def queue_prompt(prompt, client_id, server_address):
    p = {"prompt": prompt, "client_id": client_id}
    headers = {"Content-Type": "application/json"}
    data = json.dumps(p).encode("utf-8")
    req = urllib.request.Request(
        "http://{}/prompt".format(server_address), data=data, headers=headers
    )
    return json.loads(urllib.request.urlopen(req).read())


def get_history(prompt_id, server_address):
    with urllib.request.urlopen(
        "http://{}/history/{}".format(server_address, prompt_id)
    ) as response:
        return json.loads(response.read())


def get_image(filename, subfolder, folder_type, server_address):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen(
        "http://{}/view?{}".format(server_address, url_values)
    ) as response:
        return response.read()


def upload_image(input_path, name, server_address, image_type="input", overwrite=True):
    with open(input_path, "rb") as file:
        multipart_data = MultipartEncoder(
            fields={
                "image": (name, file, "image/png"),
                "type": image_type,
                "overwrite": str(overwrite).lower(),
            }
        )

        data = multipart_data
        headers = {"Content-Type": multipart_data.content_type}
        request = urllib.request.Request(
            "http://{}/upload/image".format(server_address), data=data, headers=headers
        )
        with urllib.request.urlopen(request) as response:
            return response.read()


def load_workflow(workflow_path):
    try:
        with open(workflow_path, "r") as file:
            workflow = json.load(file)
            return json.dumps(workflow)
    except FileNotFoundError:
        print(f"The file {workflow_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"The file {workflow_path} contains invalid JSON.")
        return None


def prompt_image_to_image(
    workflow_path, input_path, comfy_server_address, output_path="./output/", save_previews=False
):
    with open(workflow_path, "r", encoding="utf-8") as workflow_api_txt2gif_file:
        prompt = json.load(workflow_api_txt2gif_file)
    filename = input_path.split("/")[-1]
    prompt.get("104")["inputs"]["image"] = filename
    file_name = generate_image_by_prompt_and_image(
        prompt, output_path, input_path, filename, comfy_server_address, save_previews
    )
    return file_name


def generate_image_by_prompt_and_image(
    prompt, output_path, input_path, filename, comfy_server_address, save_previews=False
):
    try:
        ws, server_address, client_id = open_websocket_connection(comfy_server_address)
        upload_image(input_path, filename, server_address)
        prompt_id = queue_prompt(prompt, client_id, server_address)["prompt_id"]
        track_progress(prompt, ws, prompt_id)
        images = get_images(prompt_id, server_address, save_previews)
        save_image(images, output_path, save_previews)
    finally:
        ws.close()
        return os.path.join(output_path, images[-1]["file_name"])


def track_progress(prompt, ws, prompt_id):
    node_ids = list(prompt.keys())
    finished_nodes = []

    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message["type"] == "progress":
                data = message["data"]
                current_step = data["value"]
                print("In K-Sampler -> Step: ", current_step, " of: ", data["max"])
            if message["type"] == "execution_cached":
                data = message["data"]
                for itm in data["nodes"]:
                    if itm not in finished_nodes:
                        finished_nodes.append(itm)
                        print(
                            "Progess: ",
                            len(finished_nodes),
                            "/",
                            len(node_ids),
                            " Tasks done",
                        )
            if message["type"] == "executing":
                data = message["data"]
                if data["node"] not in finished_nodes:
                    finished_nodes.append(data["node"])
                    print(
                        "Progess: ",
                        len(finished_nodes),
                        "/",
                        len(node_ids),
                        " Tasks done",
                    )

                if data["node"] is None and data["prompt_id"] == prompt_id:
                    break  # Execution is done
        else:
            continue
    return


# 从history通过prompt_id找到图片
# TODO: (warning!!!) prompt_id要保证每次都不一样
# TODO: (warning!!!) 不知道是否大规模运行，history多了后会导致卡顿，可能需要清理机制
# TODO: 固定模板应该可以不用遍历 节省时间
def get_images(prompt_id, server_address, allow_preview=False):
    output_images = []

    history = get_history(prompt_id, server_address)[prompt_id]
    for node_id in history["outputs"]:
        node_output = history["outputs"][node_id]
        if "images" in node_output:
            output_data = {}
            for image in node_output["images"]:
                if allow_preview and image["type"] == "temp":
                    preview_data = get_image(
                        image["filename"],
                        image["subfolder"],
                        image["type"],
                        server_address,
                    )
                    output_data["image_data"] = preview_data
                if image["type"] == "output":
                    image_data = get_image(
                        image["filename"],
                        image["subfolder"],
                        image["type"],
                        server_address,
                    )
                    output_data["image_data"] = image_data
                output_data["file_name"] = image["filename"]
                output_data["type"] = image["type"]
                output_images.append(output_data)

    return output_images


def save_image(images, output_path, save_previews):
    #   for itm in images:
    #       directory = os.path.join(output_path, 'temp/') if itm['type'] == 'temp' and save_previews else output_path
    #       os.makedirs(directory, exist_ok=True)
    #       try:
    #           image = Image.open(io.BytesIO(itm['image_data']))
    #           image.save(os.path.join(directory, itm['file_name']))
    #       except Exception as e:
    #           print(f"Failed to save image {itm['file_name']}: {e}")
    # TODO: 这个逻辑不怎么好看 但应该不会造成隐患
    itm = images[-1]
    os.makedirs(output_path, exist_ok=True)
    try:
        image = Image.open(io.BytesIO(itm["image_data"]))
        image.save(os.path.join(output_path, itm["file_name"]))
    except Exception as e:
        print(f"Failed to save image {itm['file_name']}: {e}")


if __name__ == "__main__":
    IMAGE_PATH = "/root/autodl-tmp/comfy_api/image_tmp/images (2).jpeg"
    OUTPUT_PATH = "./output/"
    output_filename = prompt_image_to_image(
        "nobel_slight_workflow_api.json",
        IMAGE_PATH,
        output_path=OUTPUT_PATH,
        save_previews=True,
    )
    print(output_filename)
