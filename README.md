<!-- PROJECT LOGO -->
<br />
<div align="center">
    <h1> &#127942 EveryoneNobel </h1>
    <img height="300" src="resources/readme/overview.png" />
</div>

<div align="center">

| **[Overview](#overview)** | **[Requirements](#requirements)** | **[Quick Start](#quick-start)** | **[Contributors](#contributors)** |
</div>

## Overview

EveryoneNobel aims to generate **Nobel Prize images for everyone**. We utilizes ComfyUI for image generation and HTML templates to display text on the images. This project serves not only as a process for generating nobel images but also as **a potential universal framework**. This framework transforms the ComfyUI-generated visuals into final products, offering a structured approach for further applications and customization.

## Requirements
### 1. Install ComfyUI
Follow the instructions in [ComfyUI repo](https://github.com/comfyanonymous/ComfyUI) to install ComfyUI. Open ComfyUI and install the missing custom nodes and models for workflow in `resources/workflow/nobel_workflow.json`.

### 2. Install requirements
``` shell
# cd to EveryoneNobel main folder
npm install
pip install -r requirements.txt
```

### 3. write .env
Create a `.env` file in the main folder with the following content:
``` shell
API_KEY=YOUR_OPENAI_API_KEY
```

## Quick Start

### 1. Start ComfyUI server
An example for starting the server.

``` shell
# cd to ComfyUI main folder
python main.py --port 6006 --listen 0.0.0.0
```

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

## Contributors
<table>
  <tr>
    <td><a href="https://github.com/16131zzzzzzzz"><img src="https://github.com/16131zzzzzzzz.png" width="60px;"/></a></td>
    <td><a href="https://github.com/AudareLesdent"><img src="https://github.com/AudareLesdent.png" width="60px;"/></a></td>
    <td><a href="https://github.com/AlchemistZoro"><img src="https://github.com/AlchemistZoro.png" width="60px;"/></a></td>
    <td><a href="https://github.com/bs001l"><img src="https://github.com/bs001l.png" width="60px;"/></a></td>
    <td><a href="https://github.com/zhoulele12"><img src="https://github.com/zhoulele12.png" width="60px;"/></a></td>
  </tr>
</table>
