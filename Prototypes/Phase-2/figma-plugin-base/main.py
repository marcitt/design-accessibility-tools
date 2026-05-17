from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from collections import deque

# uvicorn main:app --reload

app = FastAPI()

import os
import json

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

commands = deque()

@app.post("/update")
async def update(data: dict):
    print(data)
    
    # save JSON to file in the repo folder
    filepath = os.path.join(os.path.dirname(__file__), "figma_nodes.json")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    
    return {"status": "ok"}

@app.post("/command")
async def receive_command(cmd: dict):
    commands.append(cmd)
    print(cmd)
    return {"status": "ok"}

@app.get("/command")
async def get_command():
    if commands:
        return {"command": commands.popleft()}
    return {"command": None}

