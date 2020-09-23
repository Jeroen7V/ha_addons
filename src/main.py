import json
import requests
from fastapi import FastAPI, Form, Response, Request

app = FastAPI()

@app.get("/")
async def index_get():
    return "Hello World!"

@app.post("/hook")
async def hook_post(request: Request):
    body_json = await request.json()
    if body_json['intent']['name'] == 'HomeSweetOff':
        url = 'https://monnikenhof.duckdns.org:8001/api/webhook/alloff'
        requests.post(url)
        print("Turned everything off.")
    elif body_json['intent']['name'] == 'HomeSweetCast':
        url = 'https://monnikenhof.duckdns.org:8001/api/webhook/tvtime'
        requests.post(url)
        print("Turned on cast.")
    return "Hello World!"