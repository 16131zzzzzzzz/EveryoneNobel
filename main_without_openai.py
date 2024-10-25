import os
import threading
import json
import argparse

from src.html_modify import modifier_html
from src.server import prompt_image_to_image

def main(name, subject, content, image_path, comfy_server_address):
    proj_dir = os.path.dirname(os.path.abspath(__file__))

    name_safe = name.replace(" ", "_")
    output_path = os.path.join(proj_dir, "output", name_safe)
    os.makedirs(output_path, exist_ok=True)
    html_template_path = "resources/frontend/canvas.html"

    output_pic_path = f"nobel_{name_safe}_{(image_path.split('/')[-1]).split('.')[0]}.jpg"
    output_pic_path = os.path.join(output_path, output_pic_path)
    output_html_path = os.path.join(proj_dir, "resources/frontend/tmp.html")

    subject_content = subject
    contribution_content = content

    # save config
    info = {
        "name": name,
        "content": subject_content,
        "image_path": image_path,
        "contribution": contribution_content,
        "output_image_path": output_pic_path,
    }
    print(info)
    json_file_path = os.path.join(
        output_path, f"info_{name}_{(image_path.split('/')[-1]).split('.')[0]}.json"
    )
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(info, json_file, ensure_ascii=False, indent=4)

    # comfy
    print("start comfy")
    output_filename = prompt_image_to_image(
        "resources/workflow/nobel_workflow.json",
        image_path,
        comfy_server_address,
        output_path=output_path,
        save_previews=True,
    )
    print("comfy image written into: ", output_filename)

    # template
    html_modifier = modifier_html(
        html_template_path, subject_content, name, contribution_content, output_filename
    )

    # save html
    html_modifier.save_changes(output_html_path)
    print("end generate image html")

    # start npm run dev thread
    def start_npm_dev(input_html_path, output_pic_path):
        os.system(f"npm run dev -- {input_html_path} {output_pic_path}")

    threading.Thread(target=start_npm_dev, args=(output_html_path, output_pic_path)).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Nobel Prize Slogan and Image.')
    parser.add_argument('--name', required=True, help='Name of the individual')
    parser.add_argument('--subject', required=True, help='Subject of the prize')
    parser.add_argument('--content', required=True, help='Contribution description')
    parser.add_argument('--image_path', required=True, help='Path to the input image')
    parser.add_argument('--comfy_server_address', default="127.0.0.1:6006", help='Address of the Comfy server')

    args = parser.parse_args()

    main(args.name, args.subject, args.content, args.image_path, args.comfy_server_address)
