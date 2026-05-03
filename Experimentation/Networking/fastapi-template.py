from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

import os
import json

# allow browser access
# TODO: best practice is to select these more carefully to avoid security issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


latest_data = {} #global is usually not best practice

@app.post("/update")
async def update(data: dict):
    global latest_data
    latest_data = data
    return {"status": "ok"}

@app.get("/state")
async def get_state():
    return latest_data