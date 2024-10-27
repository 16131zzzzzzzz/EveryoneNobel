# ComfyUI Models
## 1. Download Models
Download all models below and put it into ComfyUI's `models` folder. 
### SD model
link: https://civitai.com/models/112902/dreamshaper-xl

path: `models/checkpoints`

### Lora model
link: https://civitai.com/models/875184?modelVersionId=979771

path: `models/loras`

### Sam model
link：https://pan.quark.cn/s/f6422ed31f96

path: `models/sams`

### Ground-Dino model
link：https://pan.quark.cn/s/269e85ea0785

path: `models/grounding-dino`

### ControlNet model 1 (Left in the workflow for lineart)
link：https://pan.quark.cn/s/bab5376acd72

path: `models/controlnet`

### ControlNet model 2 (Right in the workflow for pose)
link：https://pan.quark.cn/s/3accad712c54

path: `models/controlnet`

### VAE model
link：https://pan.quark.cn/s/da810e21331e

path: `models/vae`

## 2. Adapt the model paths
Adapt the model paths in the workflow nodes below to the your own path.

[![sdxl and lora](https://img.picgo.net/2024/10/27/1280X1280-13420f8812ec103a9.png)](https://www.picgo.net/image/1280X1280-%281%29.oqa7JG)

[![controlnets](https://img.picgo.net/2024/10/27/7fc490b0-5923-4dbc-a650-a3d31374050ee32f3f55b2429e59.png)](https://www.picgo.net/image/7fc490b0-5923-4dbc-a650-a3d31374050e.oqahXk)

[![sam1](https://img.picgo.net/2024/10/27/7787472d-c1b0-4947-896b-928146f3aabba60dd8f63e87adf4.png)](https://www.picgo.net/image/7787472d-c1b0-4947-896b-928146f3aabb.oqaOlw)

[![sam2](https://img.picgo.net/2024/10/27/15113787-baab-4a02-99ee-eccdd0011c11c978a7fda8fae2cd.png)](https://www.picgo.net/image/15113787-baab-4a02-99ee-eccdd0011c11.oqaF5l)

## 3. Save as API format
Run ComfyUI locally in your browser. Once it’s running, go to the settings and enable the "Dev Mode Options". You can export the workflow in API format as a JSON file. Use this exported JSON to replace the original resources/workflow/nobel_workflow.json (don't change the json name).
