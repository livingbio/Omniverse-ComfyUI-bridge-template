# GliaCloud Co. Ltd. x NVIDIA Omniverse Collaboration
---------------------
This extension template extracts and streams ground truth data from Omnivsers viewport to ComfyUi, including Depth Maps, Segmentation detection, normal...

```
    response_model.output_paths = {
        "rgb": join_with_replace(replicator_data_path, rgb_identifier),
        "normals": join_with_replace(replicator_data_path, normals_identifier),
        "depth": join_with_replace(replicator_data_path, depth_identifier),
        "inst_id_seg": join_with_replace(replicator_data_path, inst_id_seg_identifier),
        "semantic_seg": join_with_replace(replicator_data_path, semantic_seg_identifier),
    }
```


# Getting started
---------------------
1. Add ext to omniverse
![add ext](demo/add-ext-search-path.png)

2. link custom node for comfyui

    for example... 
    ```
    ln -s ./exts/omni.comfyui.connector.core-0.1.0/omni/comfyui/connector/core/omni_nodes.py (Your_ComfyUI_PATH)/custom_nodes/omni_nodes.py
    ```

# Using the extension
----------------------
![extension demo](demo/extension_demo.gif)


# Project Structure
----------------------
```
Omniverse-ComfyUI-bridge-template/
├── demo/
│   ├── add-ext-search-path.png
│   └── extension_demo.gif
│
├── exts/
│   ├── omni.comfyui.connector.core-0.1.0/
│   │   ├── config/
│   │   ├── data/
│   │   ├── docs/
│   │   ├── icons/
│   │   └── omni/
│   │       └── comfyui/
│   │           └── connector/
│   │               └── core/
│   │
│   ├── omni.example.airoomgenerator/
│   ├── omni.kit.browser.reshade-0.3.12/
│   └── omni.usd.nucleus.organizer-0.1.0/
│
├── tools/
│   ├── packman/
│   │   ├── bootstrap/
│   │   └── config.packman.xml
│   │
│   └── scripts/
│       ├── link_app.py
│       └── public/
│
├── LICENSE
├── README.md
├── link_app.bat
└── link_app.sh
```

## Extension Structure (omni.comfyui.connector.core)

The main extension follows this structure:

```
omni.comfyui.connector.core-0.1.0/
├── config/
│   ├── extension.gen.toml
│   └── extension.toml
│
├── data/
│   ├── omni_workflow.json
│   ├── preview.png
│   └── screenshot.png
│
├── docs/
│   ├── CHANGELOG.md
│   └── README.md
│
├── icons/
│   └── icon.svg
│
├── omni/
│   └── comfyui/
│       └── connector/
│           └── core/
│               ├── __init__.py
│               ├── extension.py
│               ├── omni_nodes.py
│               └── use_replicator.py
│
└── README.md
```

# To Do
----------------------
- [ ] Animation Start Frame & End Frame Control  
- [ ] OpenPose Detect  
- [ ] Edge Detect
