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

## Contributors
<table>
  <tr>
    <td><a href="https://github.com/16131zzzzzzzz"><img src="https://github.com/16131zzzzzzzz.png" width="60px;"/></a></td>
  </tr>
</table>