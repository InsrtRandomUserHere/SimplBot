import discord
import os
from discord.ext import commands

embedColor = discord.Colour.from_rgb(107, 37, 249)


class OwnerCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send(f"{extension}.py Unloaded")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension}.py Loaded")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send("Cog Reloaded")

    @commands.command(aliases=["ownerhelp"])
    @commands.is_owner()
    async def help2(self, ctx):
        embed = discord.Embed(title="Owner Help Menu", colour=embedColor)
        cogs = [file for file in os.listdir("cogs") if file.endswith(".py")]
        embed.add_field(name="Cog File Names", value=f"`"*3+"\n".join(cogs)+"`"*3)
        embed.add_field(name="Commands", value="```load <CogFile>\nunload <CogFile>\nreload <CogFile>```")
        await ctx.send(embed=embed)

    @commands.command(name="shutdown")
    @commands.is_owner()
    async def shut_down(self, ctx):
        await ctx.send("Now shutting down")
        offline_log = self.client.get_channel(790619786672734249)
        await offline_log.send("🔴 Shutting down by command")
        await self.client.logout()

    @commands.command()
    @commands.is_owner()
    async def commandcount(self, ctx):
        commandsTotal = len(self.client.commands)
        await ctx.send(f"{commandsTotal} commands!")

    @commands.command(name="eval")
    @commands.is_owner()
    async def evl(self, ctx, *, code):
        await ctx.send(eval(code))


def setup(client):
    client.add_cog(OwnerCmds(client))
