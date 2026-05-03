"""
Ollama + VLM using llava

References:
Ollama Python library: https://github.com/ollama/ollama-python
PIL base64 encoding: https://www.sqlpey.com/python/top-4-methods-to-convert-pil-image-to-base64-string/
GPT-5 for prompt generation

Findings:
Overall poor results - bad accuracy, precision and generalisability.
Motivated moving away from a VLM approach.
"""

import ollama
import base64
import pyautogui
import time
from PIL import ImageGrab
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

TR = 0.574519231
TIME_DELAY = 0.45
BBOX = (0, 0, 2560, 1664)  

# wait a few seconds to switch to figma window
time.sleep(5)

# capture a screenshot
screen = ImageGrab.grab(bbox=BBOX)
screen.save("screenshot.png", 'PNG')

def encode_image(path):
    """Base64 encode an image for vision models"""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
image_b64 = encode_image("screenshot.png")

prompt_version_one = """
You are a visual layout analysis tool.

The input image is a screenshot of the Figma application window.

Task:
Visually estimate the bounding boxes of the following UI regions in the image:
- canvas
- left sidebar
- right sidebar
- top bar
- toolbar

Rules:
- Use pixel coordinates relative to the image.
- The coordinate system starts at the top-left of the image (0, 0).
- Bounding boxes should be in the form:
  {x, y, width, height}
- If an estimate is required, make your best visual estimate.
- Do NOT explain what the UI elements are.
- Do NOT say "cannot determine".
- If uncertain, still provide an estimate and mark confidence as "low".

Output:
Return a single JSON object with this structure:

{
  "canvas": {...},
  "left_sidebar": {...},
  "right_sidebar": {...},
  "topbar": {...},
  "toolbar": {...}
}

"""

prompt_version_two = """

You are performing visual layout analysis on a screenshot of the Figma desktop application.

Important constraint:
UI regions occupy space and reduce the available area for regions below or beside them.

Layout order (top to bottom, outside to inside):
1. Topbar occupies space at the very top of the window.
2. Toolbar occupies space directly below the topbar.
3. Left sidebar occupies space on the left, below the toolbar.
4. Right sidebar occupies space on the right, below the toolbar.
5. Canvas occupies all remaining central space.

Rules:
- All regions must be non-overlapping.
- The canvas must NOT include any pixels from the topbar, toolbar, or sidebars.
- Coordinates are pixel values relative to the image.
- Origin (0,0) is the top-left corner of the image.
- If exact boundaries are unclear, estimate visually.

Output:
Return ONLY valid JSON with bounding boxes in this format:

{
"topbar": {"x": int, "y": int, "width": int, "height": int},
"toolbar": {"x": int, "y": int, "width": int, "height": int},
"left_sidebar": {"x": int, "y": int, "width": int, "height": int},
"right_sidebar": {"x": int, "y": int, "width": int, "height": int},
"canvas": {"x": int, "y": int, "width": int, "height": int}
}

"""

response = ollama.chat(
    model="llava:7b",
    messages=[
        {
            "role": "user",
            "content": f"{prompt_version_two}",
            "images": [image_b64]
        }
    ]
)

print(response["message"]["content"])