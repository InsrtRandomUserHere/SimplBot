import discord
from discord.ext import commands, tasks
import json
from itertools import cycle

embedColor = discord.Colour.from_rgb(107, 37, 249)


construction = ["Currenly under maintenance"]
normal = ['sb/help']
status = cycle(normal)


class GenStuff(commands.Cog):

    def __init__(self, client):
        self.client = client



    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))
	

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print("Bot is now online")
        onlinelog = self.client.get_channel(790619786672734249)
        await onlinelog.send("🟢 Now Online")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = self.client.get_channel(790618964245348362)
        embed = discord.Embed(title='Simple Bot join logs', description=f"***{guild.name}*** has added **Simple Bot!**", color = embedColor)
        await channel.send(embed=embed)




def setup(client):
    client.add_cog(GenStuff(client))