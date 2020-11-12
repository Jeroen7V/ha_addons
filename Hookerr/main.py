import json
import requests
from fastapi import FastAPI, Form, Response, Request

app = FastAPI()
endpoints = {}

try:
    with open('/data/options.json') as file:
        endpoints = json.load(file)
except FileNotFoundError:
    print ("No config file found.")
    exit(1)
except json.decoder.JSONDecodeError:
    print ("Syntax error in the config file.")
    exit(1)

@app.get("/")
async def index_get():
    return endpoints

if 'get' in endpoints:
    @app.get("/get")
    async def endpoints_get(target: str = ""):
        found = False
        for endpoint in endpoints['get']:
            if str.upper(target) == str.upper(endpoint):
                found = True
                webhook = "http://homeassistant:8123/api/webhook/" + endpoint
                try:
                    response = requests.post(webhook)
                    print("Called " + response.url + " with return code " + str(response.status_code) + ".")
                    return({"url": response.url, "return code": response.status_code})
                except requests.exceptions.ConnectionError as e:
                    print(e)
                    return({"error": "Couldn't reach the HA webhook. Check logs."})
        if not found:
            print("Endpoint " + target + " was not found in the config.")
            return({"error": "Endpoint " + target + " was not found in the config."})