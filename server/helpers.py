from settings import *
from aiohttp import ClientSession

discord_api = 'https://discord.com/api/v10'
roblox_api = 'https://apis.roblox.com/oauth'
redirect_uris = {
    'dev': '',
    'prod': '',
    'discord_dev': 'http://localhost:3000/authorize/discord',
    'roblox_dev': 'http://localhost:3000/authorize/roblox'
}
discord_redirect = redirect_uris['discord_dev']
roblox_redirect = redirect_uris['roblox_dev']

class ShallowAuth:
    def __init__(self, data:dict):
        self.access_token = data.get('access_token')
        self.refresh_token = data.get('refresh_token')

class DiscordUser:
    def __init__(self, data:dict):
        self.id = data.get('id')
        self.username = data.get('username')
        self.avatar = f"https://cdn.discordapp.com/avatars/{self.id}/{data.get('avatar')}.webp"
        
class RobloxUser:
    def __init__(self, data:dict):
        self.id = data.get('sub')
        self.username = data.get('name')
        self.avatar = data.get('picture')

def success(state:bool=True, message:str=None, data:dict=None):
    response = {'success': state}
    if message:
        response['message'] = message
    if data:
        for key in data.keys():
            response[key] = data[key]
    return response

async def get_discord_user(access_token) -> DiscordUser|None:
    async with ClientSession() as session:
        headers = {'Authorization': f'Bearer {access_token}'}
        response = await session.get(f'{discord_api}/users/@me', headers=headers)
        data:dict = await response.json()
        if not data.get('id'):
            print(data)
            return
        
        return DiscordUser(data)

async def get_roblox_user(access_token) ->RobloxUser|None:
    async with ClientSession() as session:
        headers = {'Authorization': f'Bearer {access_token}'}
        response = await session.get(f'{roblox_api}/v1/userinfo', headers=headers)
        data:dict = await response.json()
        print(data)
        if not data.get('sub'):
            print(data)

        return RobloxUser(data)

async def roblox_exchange_code(code) -> ShallowAuth | None:
    async with ClientSession() as session:
        package = {
            'code': code,
            'grant_type': 'authorization_code',
            'client_id': ROBLOX_CLIENT_ID,
            'client_secret': ROBLOX_CLIENT_SECRET
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = await session.post(f'{roblox_api}/v1/token', headers=headers, data=package)
        data:dict = await response.json()
        print(data)
        if not data.get('access_token'):
            return
        return ShallowAuth(data)

async def discord_exchange_code(code) -> ShallowAuth | None:
    async with ClientSession() as session:
        print(code)
        package = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': discord_redirect,
            'client_id': DISCORD_CLIENT_ID,
            'client_secret': DISCORD_CLIENT_SECRET
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = await session.post(f'{discord_api}/oauth2/token', data=package, headers=headers)
        data:dict = await response.json()
        if not data.get('access_token'):
            print(data)
            return
        return ShallowAuth(data)