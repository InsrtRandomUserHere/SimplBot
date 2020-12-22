import discord
from discord.ext import commands
from discord.ext.commands import BucketType

class economy(commands.Cog):

    def __init__(self, client):
        self.client = client
        

def setup(client):
	client.add_cog(economy(client)) 