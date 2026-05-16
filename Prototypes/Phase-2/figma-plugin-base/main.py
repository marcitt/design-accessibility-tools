from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from collections import deque

app = FastAPI()

import os
import json

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# commands = deque()

@app.post("/command")
async def receive_command(cmd: dict):
    # commands.append(cmd)
    print(cmd)
    return {"status": "ok"}

# @app.get("/command")
# async def get_command():
#     if commands:
#         return {"command": commands.popleft()}
#     return {"command": None}

