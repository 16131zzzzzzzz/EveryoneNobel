<!-- PROJECT LOGO -->
<br />
<div align="center">
    <h1> &#127942 EveryoneNobel </h1>
    <img height="300" src="resources/readme/overview.png" />
</div>

<div align="center">

| **[Overview](#overview)** | **[News](#news)** | **[Requirements](#requirements)** | **[Quick Start](#quick-start)** | **[Contributors](#contributors)** |
</div>

## 💡 Overview

EveryoneNobel aims to generate **Nobel Prize images for everyone**. We utilizes ComfyUI for image generation and HTML templates to display text on the images. This project serves not only as a process for generating nobel images but also as **a potential universal framework**. This framework transforms the ComfyUI-generated visuals into final products, offering a structured approach for further applications and customization.

We share how we build the entire app and sell the product in 30 hours in this blog [here](https://mp.weixin.qq.com/s/t3v-h1MzpFKuh0RCMRmjEg).

You could generate the picture without text [here](https://civitai.com/models/875184?modelVersionId=979771).

<div align="center">
    <img width="800" src="resources/readme/result_allinone_small.png" />
</div>

## 🔥 News
- Added new requirements websocket-client==0.58.0
- We upload the models to enable easier usage of ComfyUI. Readme here in [ComfyUI Models](README_model.md)
- Some issues have mentioned the workflow problems. A new file `nobel_workflow_for_install.json` here in `resources/workflow/` used for missing node installation.
- Quick Start step 1 readme has been adapted. The ComfyUI server need to use the python inside ComfyUI.
- Our second QQ group 348210641 is now open! You're welcome to join for discussions on all issues.

<div align="center">
    <img width="300" src="resources/readme/qq2.jpg" />
</div>

## 🎬 Requirements
### 1. Install ComfyUI
Follow the instructions in [ComfyUI repo](https://github.com/comfyanonymous/ComfyUI) to install ComfyUI. Open ComfyUI and install the missing custom nodes and models for workflow in `resources/workflow/nobel_workflow_for_install.json`. Run the workflow to check if the installation is successful. Then save the API format workflow json and replace `resources/workflow/nobel_workflow.json`.

This process is quite complex so we give out more details in [ComfyUI Models](README_model.md).

### 2. Install requirements
``` shell
# cd to EveryoneNobel main folder
npm install
pip install -r requirements.txt
```

### 3. write .env (optional when using main_without_openai.py) 
Create a `.env` file in the main folder with the following content:
``` shell
API_KEY=YOUR_OPENAI_API_KEY
```

## 🚀 Quick Start
Make sure that you are familiar with ComfyUI and Python, or it will take a long time. If you are not familiar, try to use liblib or civitai.
### 1. Start ComfyUI server
An example for starting the server.

``` shell
# cd to ComfyUI main folder
{ComfyUI_python} main.py --port 6006 --listen 0.0.0.0
```

(NEW) The {ComfyUI_python} is the path to the python inside your ComfyUI. For me, it is the python.exe under python_embeded folder in ComfyUI.

### 2. Run main.py

An example
```shell
python main.py \
  --name "somebody" \
  --subject "2024 nobel prize" \
  --content "Do nothing" \
  --image_path "resources/test/test.jpg" \
  --comfy_server_address "127.0.0.1:6006"
```
Parameter Explanations:
- `--name`: The name of the individual.
- `--subject`: The subject of the prize.
- `--content`: Description contribution of the individual. (AI will use this to generate the text at the bottom of the image)
- `--image_path "resources/test/test.jpg"`: The file path of the input image
- `--comfy_server_address "127.0.0.1:6006"`: Sets the address of the ComfyUI server that will handle the image generation.

(NEW) Example for not using openai api to generate text:
```shell
python main_without_openai.py \
  --name "somebody" \
  --subject "2024 nobel prize" \
  --content "Do nothing" \
  --image_path "resources/test/test.jpg" \
  --comfy_server_address "127.0.0.1:6006"
```

## 🔧 Contributors
<table>
  <tr>
    <td><a href="https://github.com/16131zzzzzzzz"><img src="https://github.com/16131zzzzzzzz.png" width="60px;"/></a></td>
    <td><a href="https://github.com/AudareLesdent"><img src="https://github.com/AudareLesdent.png" width="60px;"/></a></td>
    <td><a href="https://github.com/AlchemistZoro"><img src="https://github.com/AlchemistZoro.png" width="60px;"/></a></td>
    <td><a href="https://github.com/bs001l"><img src="https://github.com/bs001l.png" width="60px;"/></a></td>
    <td><a href="https://github.com/zhoulele12"><img src="https://github.com/zhoulele12.png" width="60px;"/></a></td>
  </tr>
</table>

## 🏄 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=16131zzzzzzzz/EveryoneNobel&type=Date)](https://star-history.com/#16131zzzzzzzz/EveryoneNobel&Date)
