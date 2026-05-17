import speech_recognition as sr
import json

from dotenv import load_dotenv
from openai import OpenAI

from system_prompt import get_system_prompt

import requests
import queue
import threading
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

    print(f"\ncommand: {reply}\n")
    return reply


running = True

# queues are thread safe data structures -> what makes them safe? why isn't a list/array safe?
# multiple threads can read and write without corrupting data -> would be an issue with arrays?
# are there any other data methods to be aware of?
audio_queue = queue.Queue()
text_queue = queue.Queue(maxsize=1)  # only keep latest command

# locks prevent two threads from accessing data at the same time which would cause corruption
# how do you know when you need a lock?


# listen thread
def listen_loop():
    with sr.Microphone() as source:
        print("Recording...")
        # r.adjust_for_ambient_noise(source, duration=1)
        while running:
            try:
                audio = r.listen(source, phrase_time_limit=8)
                audio_queue.put(audio)
            except sr.WaitTimeoutError:
                continue


# transcription thread
def transcribe_loop():
    while running or not audio_queue.empty():
        try:
            audio = audio_queue.get(timeout=1)
        except queue.Empty:
            continue

        try:
            text = r.recognize_google(audio)
            print(f'\n\ntranscription: "{text}"')
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Speech recognition error:", e)
            continue

        if len(text.strip()) < 2:
            continue

        # keep only latest command
        if text_queue.full():
            try:
                text_queue.get_nowait()
            except queue.Empty:
                pass

        text_queue.put(text)


last_call_time = 0


def llm_loop():
    global last_call_time

    while running or not text_queue.empty():

        try:
            text = text_queue.get(timeout=1)
        except queue.Empty:
            continue
        if not text:
            continue
        if time.time() - last_call_time < 1.0:
            continue

        last_call_time = time.time()

        # load figma nodes data
        system_prompt = get_system_prompt()

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


print("\n" * 30)
listen_thread = threading.Thread(target=listen_loop)
transcribe_thread = threading.Thread(target=transcribe_loop)
llm_thread = threading.Thread(target=llm_loop)

listen_thread.start()
transcribe_thread.start()
llm_thread.start()

try:
    input("Press Enter to stop...\n")
except KeyboardInterrupt:
    print("Interrupted")
finally:
    running = False


running = False

listen_thread.join()
transcribe_thread.join()
llm_thread.join()

print("Stopped.")
