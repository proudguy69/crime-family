from settings import *
from aiohttp import ClientSession

discord_api = 'https://discord.com/api/v10'
roblox_api = 'https://apis.roblox.com/oauth'
redirect_uris = {
    'dev': '',
    'prod': '',
    'dev_server': 'http://localhost:8000/authorize',
    'roblox': 'http://localhost:8000/authorize/roblox'
}
discord_redirect = redirect_uris['dev_server']
roblox_redirect = redirect_uris['roblox']

def success(state:bool=True, message:str=None, data:dict=None):
    response = {'success': state}
    if message:
        response['message'] = message
    if data:
        for key in data.keys():
            response[key] = data[key]
    return response

async def get_discord_user(access_token):
    async with ClientSession() as session:
        headers = {'Authorization': f'Bearer {access_token}'}
        response = await session.get(f'{discord_api}/users/@me', headers=headers)
        return await response.json()

async def get_roblox_user(access_token):
    async with ClientSession() as session:
        headers = {'Authorization': f'Bearer {access_token}'}
        response = await session.get(f'{roblox_api}/v1/userinfo', headers=headers)
        return await response.json()

async def roblox_exchange_code(code):
    async with ClientSession() as session:
        data = {
            'code': code,
            'grant_type': 'authorization_code',
            'client_id': ROBLOX_CLIENT_ID,
            'client_secret': ROBLOX_CLIENT_SECRET
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = await session.post(f'{roblox_api}/v1/token', headers=headers, data=data)
        return await response.json()

async def discord_exchange_code(code):
    async with ClientSession() as session:
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': discord_redirect,
            'client_id': DISCORD_CLIENT_ID,
            'client_secret': DISCORD_CLIENT_SECRET
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = await session.post(f'{discord_api}/oauth2/token', data=data, headers=headers)
        return await response.json()