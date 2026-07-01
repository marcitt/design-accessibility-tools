import requests
import os
from dotenv import load_dotenv

load_dotenv()

FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")
FILE_KEY = os.getenv("FILE_KEY")

headers = {
    "X-Figma-Token": FIGMA_TOKEN
}

url = f"https://api.figma.com/v1/files/{FILE_KEY}"
res = requests.get(url, headers=headers)

print(res.status_code)
print(res.json().keys())

data = res.json()
print(data.keys())
print(data["document"])
print(data["document"]["children"])

# for key in data.keys():
#     print(data[key])