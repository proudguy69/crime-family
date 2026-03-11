from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aiohttp import ClientSession
from helpers import *

origins = [
    'http://localhost:3000'
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/authorize')
async def authorize(code:str):
    if not code:
        return success(False, 'No code provided in url')
    
    data:dict = await discord_exchange_code(code)
    user = await get_discord_user(data.get('access_token'))
    return user

@app.get('/authorize/roblox')
async def roblox_auth(code):
    data:dict = await roblox_exchange_code(code)
    user = await get_roblox_user(data.get('access_token'))
    
    return user