import speech_recognition as sr
import json

from dotenv import load_dotenv
from openai import OpenAI

import requests

# load figma nodes data
with open("figma_nodes.json", "r") as f:
    figma_data = json.load(f)

nodes = figma_data["nodes"]
layer_names = [node["name"] for node in nodes]
print(layer_names)

# load openai
load_dotenv()
client = OpenAI()

from system_prompt import get_system_prompt

system_prompt = get_system_prompt(layer_names)

r = sr.Recognizer()

r.energy_threshold = 150  # lower = more sensitive
# found that adjusting this really helped!

# if this is too high quiet speech or short commands won't get picked up as speech
# if it is too low background noise will get picked up as speech

r.dynamic_energy_threshold = False


with sr.Microphone() as source:
    print("Recording...")
    # r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source, phrase_time_limit=10)

text = r.recognize_google(audio)
print(">>", text)

input_list = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": text},
]

# response = client.responses.create(
#     model="gpt-4o-mini",
#     input=input_list
# )

response = client.responses.create(model="gpt-3.5-turbo", input=input_list)

msg = response.output[0]
text = msg.content[0].text
print(text)

if text.startswith("{{") and text.endswith("}}"):
    text = text[1:-1]

try:
    json_data = json.loads(text)
except json.JSONDecodeError:
    print(f"Invalid JSON, skipping: {text}")
    json_data = {"type": "unknown", "raw": text}

requests.post("http://localhost:8000/command", json=json_data)
