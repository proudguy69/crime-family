from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from models import *
from helpers import *

origins = [
    'http://localhost:3000'
]

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models":['models']},
    generate_schemas=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/authorize/discord')
async def discord_auth(code:str):
    shallow_auth:ShallowAuth = await discord_exchange_code(code)
    if not shallow_auth:
        return success(False, message="Failed to obtain access token")
    user_data = await get_discord_user(shallow_auth.access_token)
    shallow_user = await User.get_or_none(discord_id=user_data.id).prefetch_related('auth')
    if shallow_user:
        auths:list[Authentication] = await shallow_user.auth.all()
        auth = auths[0]
        await auth.delete()
        await shallow_user.delete()
    user = await User.create(discord_username=user_data.username, discord_id=user_data.id, discord_avatar_url=user_data.avatar)
    auth = await Authentication.create(web_token=Authentication.gen_token(), discord_token=shallow_auth.access_token, user=user)
    return success(data={'web_token':auth.web_token, 'user':user})

@app.get('/authorize/roblox')
async def roblox_auth(code):
    shallow_auth:ShallowAuth = await roblox_exchange_code(code)
    if not shallow_auth:
        return success(False, message="Failed to obtain access token")
    user = await get_roblox_user(shallow_auth.access_token)
    return success()

@app.get('/authenticate')
async def authenticate(authorization:str=Header(None)):
    auth = await Authentication.get_or_none(web_token=authorization)
    if not auth:
        return success(False, message="authentication not found")
    user = await auth.user
    return success(data={"user":user})