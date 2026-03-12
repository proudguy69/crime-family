from tortoise import Model, fields
from secrets import token_hex

class Authentication(Model):
    id = fields.IntField(primary_key=True)
    web_token = fields.TextField()
    discord_token = fields.TextField()
    roblox_refreshtoken = fields.TextField(null=True)
    user:User = fields.ForeignKeyField('models.User', related_name='auth')

    @classmethod
    def gen_token(cls):
        token = token_hex()
        return token


class User(Model):
    id = fields.IntField(primary_key=True)

    discord_username = fields.CharField(max_length=32)
    discord_id = fields.IntField()
    discord_avatar_url = fields.TextField()

    roblox_username = fields.CharField(max_length=32, null=True)
    roblox_id = fields.IntField(null=True)
    roblox_avatar_url = fields.TextField(null=True)
    auth = fields.ReverseRelation['Authentication']



