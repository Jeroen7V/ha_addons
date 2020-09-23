import json
import requests
from fastapi import FastAPI, Form, Response, Request

app = FastAPI()

@app.get("/")
async def index_get():
    return "Hello World!"
    
@app.get("/shellylocal")
async def shellylocal_get(location: str = ""):
    response = "Done nothing!"
    if str.upper(location) == 'HALLDOWN':
        url = 'http://192.168.1.4:8123/api/webhook/alloff'
        requests.post(url)
        response = "Turned everything off."
    elif str.upper(location) == 'HALLUP':
        url = 'http://192.168.1.4:8123/api/webhook/halltoggle'
        requests.post(url)
        response = "Toggled hall lights."
    elif str.upper(location) == 'BEDROOM':
        url = 'http://192.168.1.4:8123/api/webhook/bedroomtoggle'
        requests.post(url)
        response = "Toggled bedroom lights."
    print(response)
    return response