"""
Reference: Claude Sonnet 4.6
"""

import json
import sys
import threading
import subprocess
import atexit
import signal
import requests
import pyautogui
from dotenv import load_dotenv
from openai import OpenAI
from system_prompt import get_system_prompt

load_dotenv()
client = OpenAI()

history = []
MAX_HISTORY = 10  # think about tweaking the history to find the optimal length - or provide a strong justification
overlay_process = None

# lock prevents two threads accessing overlay_process simultaneously
overlay_lock = threading.Lock()

# pyautogui safety margin — stops mouse hitting screen edge
pyautogui.FAILSAFE = True


# these are added to try to ensure safe termination of any subprocesses once the interpreter exits
# def cleanup_handler(signum, frame):
#     cleanup()
#     sys.exit(0)


# signal.signal(signal.SIGTERM, cleanup_handler)
# signal.signal(signal.SIGINT, cleanup_handler)


def cleanup():
    with overlay_lock:
        if overlay_process:
            overlay_process.terminate()


atexit.register(cleanup)


def process_command(text, system_prompt):
    global history  # references the global history array

    history.append({"role": "user", "content": text})

    if len(history) > MAX_HISTORY:
        # slice starting from the end of the list - keeps the N most recent history elements
        history = history[-MAX_HISTORY:]

    # chat endpoint - other endpoints include .images or .audio
    #

    response = client.chat.completions.create(
        model="o4-mini",  # low latency model
        reasoning_effort="low",
        messages=[{"role": "system", "content": system_prompt}, *history],
        response_format={"type": "json_object"},
        # * is used for unpacking - it takes a list and spreads outs out individually
    )

    # response.choices contains the list of possible responses
    # strip is used to remove any trailing whitespace or \n

    reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": reply})

    # history includes both the user command and the model reply
    # -> this helps the model to understand what it did in order to be successful

    print(f"\ncommand: {reply}\n")
    return reply


def handle_system_command(cmd):
    global overlay_process

    action = cmd.get("action")

    with overlay_lock:
        if action == "show":
            if overlay_process is None:
                overlay_process = subprocess.Popen(["python", "overlay.py"])
                print("overlay started")

        elif action == "hide":
            if overlay_process:
                overlay_process.terminate()
                overlay_process = None
                print("overlay stopped")

        elif action == "toggle":
            if overlay_process:
                overlay_process.terminate()
                overlay_process = None
                print("overlay stopped")
            else:
                overlay_process = subprocess.Popen(["python", "overlay.py"])
                # overlay_process variable is a reference back to the process
                # this allows the process to be controlled programmatically (e.g. in this script)
                # totally seperate process different to having the same thread (e.g. the LLM thread)
                print("overlay started")


def handle_mouse_command(cmd):
    # mouse control as fallback for UI interactions not possible via Figma API
    action = cmd.get("action")

    try:
        if action == "move":
            x = cmd.get("x")
            y = cmd.get("y")
            pyautogui.moveTo(x, y, duration=0.3)

        elif action == "click":
            x = cmd.get("x")
            y = cmd.get("y")
            pyautogui.click(x, y)

        elif action == "double_click":
            x = cmd.get("x")
            y = cmd.get("y")
            pyautogui.doubleClick(x, y)

        elif action == "right_click":
            x = cmd.get("x")
            y = cmd.get("y")
            pyautogui.rightClick(x, y)

        elif action == "drag":
            x1 = cmd.get("x1")
            y1 = cmd.get("y1")
            x2 = cmd.get("x2")
            y2 = cmd.get("y2")
            pyautogui.moveTo(x1, y1)
            pyautogui.dragTo(x2, y2, duration=0.5)

        print(f"mouse: {action} at ({cmd.get('x')}, {cmd.get('y')})")

    except Exception as e:
        print(f"mouse error: {e}")


def llm_loop(text):
    system_prompt = get_system_prompt()
    text_out = process_command(
        text, system_prompt
    )  # sends the transcript to the LLM to be processed

    # handles edge case where LLM accidently wrpas response in dpuble curly braces {{...}}
    if text_out.startswith("{{") and text_out.endswith("}}"):
        text_out = text_out[1:-1]

    try:
        json_data = json.loads(text_out)
    except json.JSONDecodeError:
        print(f"invalid json, skipping: {text_out}")  # printing enables debugging
        json_data = {"level": "figma", "type": "unknown", "raw": text_out}

    level = json_data.get("level", "figma")
    # figma as a fallback if level doesn't exist

    if level == "system":
        handle_system_command(json_data)
    elif level == "mouse":
        handle_mouse_command(json_data)
    # if it is a figma command it is sent to Figma sandbox to be dealt with there:
    else:
        try:
            requests.post("http://localhost:8000/command", json=json_data)
        except requests.RequestException as e:
            print("error sending command:", e)


print("\n" * 30)
print("type a command, ctrl+c to stop")

try:
    while True:
        text = input(">> ")

        # only runs if an input is provided:

        if text.strip():
            # LLM loop run in a seperate thread
            t = threading.Thread(target=llm_loop, args=(text.strip(),))
            t.start()  # start thread
            # target = function to run
            # args = arguments to pass
            # arguments need to be a tuple (text.strip(),) creates a tuple with one item

except KeyboardInterrupt:
    print("stopped.")
