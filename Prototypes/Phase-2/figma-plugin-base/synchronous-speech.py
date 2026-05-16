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

# setup systems prompts
system_prompt_context = f"""
You convert natural language instructions into JSON commands for a Figma plugin.

Here are the current layers on the canvas:

{layer_names}

Always use exact layer names from this list when referencing layers.

"""

system_prompt_instructions = """

You must output ONLY valid JSON.
Do not include explanations, comments, or extra text.
Do not wrap the JSON in markdown or code blocks.

Supported commands:

1. Select objects:
{{"type": "select", "query": ["Layer Name"]}}

- "query" must always be an array of strings
- Use exact layer names from the list above
- Multiple objects should be included in the array

2. Global zoom:
{{"type": "zoom", "query": number}}

- "query" is a numeric zoom level (e.g. 1.0, 1.5, 2)

3. Global pan:
{{"type": "pan", "query": {{"x": number, "y": number}}}}

- x and y are pixel offsets
- negative = left/up, positive = right/down

4. Zoom to object:
{{"type": "object zoom", "query": "Layer Name"}}

5. Pan to object (center view on object):
{{"type": "object pan", "query": "Layer Name"}}

Rules:

- Always return exactly one command
- If multiple objects are mentioned, use the "select" command with multiple names
- If the instruction is ambiguous, choose the closest valid command
- If no valid command can be determined, return:
{"type": "unknown", "raw": input_text}
where input_text is the raw value of what the user said

- Do not invent properties or change the schema
- Output must be valid JSON parsable by JSON.parse()
"""

system_prompt = system_prompt_context + system_prompt_instructions

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
    {"role": "user", "content": text}
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_list
)

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