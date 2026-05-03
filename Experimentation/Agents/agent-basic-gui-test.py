from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
import pyautogui
import time

@tool
def move_cursor(x: int, y: int):
    """Move the cursor relative to current position"""
    pyautogui.moveRel(x, y, duration=0.2)
    return f"Moved cursor by ({x}, {y})"

@tool
def click(x=None, y=None, button='left'):
    """Click"""
    pyautogui.click(x=x, y=y, button=button)
    return f"Mouse clicked"

@tool
def type_text(text: str):
    """Type text using the keyboard."""
    pyautogui.typewrite(text)
    return f"Typed text: {text}"

# @tool
# def draw_bezier(b1_x,b1_y, b2_x, b2_y, ratio=0.5, l1=10, l2=10):
#     """Draw a bezier with starting coordinate (b1_x,b1_y), a bend point initiated at the given ratio, e.g. 0.5 = midway between
#     and a bend extruded by l1=10, l2=10"""
#     return f"Here is a description of the bezier: {b1_x,b1_y, b2_x, b2_y, ratio, l1, l2}"


model = ChatOllama(model="mistral", temperature=0).bind_tools([move_cursor, click, type_text])

messages = [SystemMessage(content="You are an assistant that can control the computer using tools."), 
            HumanMessage(content="Move mouse 100px left, move mouse 100px up, click and then type hello")]

response = model.invoke(messages)
print("Response:", response)

# need to look at the response processing in a bit more depth 
# how does it typically work - what are different styles?

