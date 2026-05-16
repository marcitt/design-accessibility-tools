import speech_recognition as sr
import json

from dotenv import load_dotenv
from openai import OpenAI

import requests

import time

history = []
MAX_HISTORY = 10

# load openai
load_dotenv()
client = OpenAI()

r = sr.Recognizer()

r.energy_threshold = 150  # lower = more sensitive
# found that adjusting this really helped!

# if this is too high quiet speech or short commands won't get picked up as speech
# if it is too low background noise will get picked up as speech

r.dynamic_energy_threshold = False


def process_command(text, system_prompt):
    global history

    history.append({"role": "user", "content": text})

    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_prompt}, *history],
    )

    reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": reply})

    print(reply)
    return reply


def identify_command():
    # load figma nodes data

    from system_prompt import get_system_prompt

    system_prompt = get_system_prompt()

    with sr.Microphone() as source:
        print("Recording...")
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=10)

    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Nothing detected, skipping")
        text = None
        return {"type": "unknown", "raw": text}

    print(">>", text)

    # input_list = [
    #     {"role": "system", "content": system_prompt},
    #     {"role": "user", "content": text},
    # ]

    # # response = client.responses.create(model="gpt-4o-mini", input=input_list)
    # response = client.responses.create(model="gpt-3.5-turbo", input=input_list)

    # msg = response.output[0]
    # text = msg.content[0].text
    # print(text)

    text_out = process_command(text, system_prompt)

    if text_out.startswith("{{") and text_out.endswith("}}"):
        text_out = text_out[1:-1]

    try:
        json_data = json.loads(text_out)
    except json.JSONDecodeError:
        print(f"Invalid JSON, skipping: {text_out}")
        json_data = {"type": "unknown", "raw": text_out}

    try:
        requests.post("http://localhost:8000/command", json=json_data)
    except requests.RequestException as e:
        print("Error sending command:", e)


i = 0

# Continuous loop
try:
    while i < 10:
        identify_command()
        time.sleep(0.5)  # small delay between recordings
        i = i + 1
except KeyboardInterrupt:
    print("Stopping voice loop.")
