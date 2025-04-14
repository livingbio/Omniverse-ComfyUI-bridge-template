# Omniverse-ComfyUI Bridge

A bridge extension that connects NVIDIA Omniverse with ComfyUI, enabling the extraction and streaming of ground truth data from Omniverse viewport to ComfyUI for enhanced AI image processing workflows.

## Overview

This extension leverages Omniverse Replicator to extract various types of data from the Omniverse viewport and makes them available to ComfyUI through custom nodes. The extracted data includes:

- RGB images (standard viewport capture)
- Normal maps
- Depth maps
- Instance ID segmentation
- Semantic segmentation

The extension provides both a simple viewport capture for single frames and a recording capability for capturing multiple frames with various data types.

## Features

- **Viewport Capture**: Capture the current viewport as a standard RGB image
- **Viewport Recording**: Record multiple frames with various data types (RGB, normals, depth, segmentation)
- **ComfyUI Integration**: Custom nodes for ComfyUI that can access the captured data

## Requirements

- NVIDIA Omniverse (Code, Create, or other compatible application)
- ComfyUI installation

## Getting Started

### 1. Add Extension to Omniverse

Add the extension search path to your Omniverse application:

![add ext](demo/add-ext-search-path.png)

### 2. Link Custom Nodes to ComfyUI

Create a symbolic link from the extension's custom nodes to your ComfyUI installation:

```bash
# Linux/macOS
ln -s ./exts/omni.comfyui.connector.core-0.1.0/omni/comfyui/connector/core/omni_nodes.py (Your_ComfyUI_PATH)/custom_nodes/omni_nodes.py

# Windows (Command Prompt as Administrator)
mklink (Your_ComfyUI_PATH)\custom_nodes\omni_nodes.py .\exts\omni.comfyui.connector.core-0.1.0\omni\comfyui\connector\core\omni_nodes.py
```

## Using the Extension

### In Omniverse

1. Load your scene in Omniverse
2. The extension automatically starts a service on `http://localhost:8111/viewport-capture`
3. Position your viewport to capture the desired view

### In ComfyUI

1. Start ComfyUI
2. Use the provided custom nodes:
   - `Screen Capture Omniverse Viewport`: Captures a single frame from the viewport
   - `Screen Record Omniverse Viewport`: Records multiple frames with various data types

![extension demo](demo/extension_demo.gif)

## Data Types

The extension extracts the following data types:

- **RGB**: Standard color image from the viewport
- **Normals**: Surface normal vectors visualized as RGB colors
- **Depth**: Distance from camera visualized as grayscale
- **Instance ID Segmentation**: Unique color for each object instance
- **Semantic Segmentation**: Color-coded semantic categories

## Project Structure

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

## To Do

- [ ] Animation Start Frame & End Frame Control
- [ ] OpenPose Detect
- [ ] Edge Detect

## License

See the [LICENSE](LICENSE) file for details.
