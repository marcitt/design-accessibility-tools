"""
test different approaches for VLMs reasoning over screenshots
"""

import ollama
import base64
import pyautogui
import time
from PIL import ImageGrab
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

#encode the screenshot
path = "cropped_screenshot.png"
with open(path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
        
prompt = """
You are given a screenshot of a Figma frame.

Image size:
- Width: 465px
- Height: 465px
- Origin (0,0) is the top-left
- x increases to the right, y increases downward

Method:
Step 1: Divide the image into a 3×3 grid.
        Label columns A–C (left to right) and rows 1–3 (top to bottom).
        Identify which cell contains the CENTER of the red square.

Step 2: Take only that cell and subdivide it again into a 3×3 grid
        using the same labels.
        Identify which sub-cell contains the CENTER of the red square.

Step 3: Assume the center of the final sub-cell is the location of the red square.
        Convert that location into pixel coordinates.

Output format (strict):
{
  "level1_cell": "<A1–C3>",
  "level2_cell": "<A1–C3>",
  "x_px": <number>,
  "y_px": <number>
}

Return only the JSON.
"""

response = ollama.chat(
    model="llava:7b",
    messages=[
        {
            "role": "user",
            "content": f"{prompt}",
            "images": [image_b64]
        }
    ]
)

print(response["message"]["content"])

path = "cropped_screenshot.png"
with open(path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
        
prompt = """
You are given an image.

Task:
1. Locate the red square.
2. Estimate the position of its CENTER as a fraction of the image:
   - x_norm in range [0, 1] from left to right
   - y_norm in range [0, 1] from top to bottom

Image size:
- Width: 465px
- Height: 465px

Output format (strict JSON):
{
  "x_norm": <number between 0 and 1>,
  "y_norm": <number between 0 and 1>
}

Do not convert to pixels.
Do not include explanations.
"""

response = ollama.chat(
    model="llava:7b",
    messages=[
        {
            "role": "user",
            "content": f"{prompt}",
            "images": [image_b64]
        }
    ]
)

print(response["message"]["content"])