import keep_alive
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import os
from datetime import datetime
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import aiohttp
#Just importing some modules



embedColor = discord.Colour.from_rgb(107, 37, 249)
#The color for embeds

intents = discord.Intents.default()



client = commands.Bot(command_prefix="sb/", intents=discord.Intents.all(), case_insensitive=True)

#Getting uptime
client.launch_time = datetime.utcnow()

#Removing default help command
client.remove_command('help')


#For loading in some cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Cog Loaded")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Cog Unloaded")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Cog Reloaded")


for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"cogs.{name}")
#End of loading of cogs

#Owner Help Menu
@client.command()
@commands.is_owner()
async def help2(ctx):
    embed = discord.Embed(
        title="Owner Help Menu",
        colour=embedColor
    )
    embed.add_field(
        name="Cog File Names",
        value="```cmd_help.py\ncmds_general.py\ncmds_stats.py\ncmds_text.py\ncmds_utility.py\ngenerals.py```"
    )
    embed.add_field(name="Commands", value="```load <CogFile>\nunload <CogFile>\nreload <CogFile>```")

    await ctx.send(embed=embed)


#leave command
@client.command()
@commands.has_permissions(kick_members=True)
async def leave(ctx):
    await ctx.send("Leaving Server")
    await ctx.guild.leave()

#Shutdown command
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Now shutting down")
    await client.logout()



#Command Error Handlers
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.purge(limit=1)
        await ctx.send("Please complete your command")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)

    elif isinstance(error, commands.CommandNotFound):
        pass

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permissions to do that")

    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have the permissions to do that")

    elif isinstance(error, commands.NotOwner):
        await ctx.send('You are not the owner. Only InsrtRandomUserHere#0001 can use this command')

    elif isinstance(error, commands.NSFWChannelRequired):
        await ctx.send(
            'This channel is not marked as NSFW. This command can only be used in a channel that is marked as NSFW')

    elif isinstance(error, commands.MemberNotFound):
        await ctx.send('That member cannot be found')

    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="You are on cooldown!", description=f"Woah! Slow down there pal! You're using this command too fast! Try this command again in **{error.retry_after:,.2f}** seconds", color=embedColor)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error",
                              description="Oh no! An error has occured while trying to do this command. You can use the `sb/report` command to report this error. If you do report this bug, also please include this:```{}```".format(
                                  error), color=embedColor)
        embed.set_thumbnail(url="https://assets.stickpng.com/images/5a81af7d9123fa7bcc9b0793.png")
        await ctx.send(embed=embed)

#Just incase i need this
"""@client.event
async def on_message(msg):"""


#This too
"""
@client.event
async def on_member_join(member):
    global joined
    joined += 1
"""

#Main Brain
keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)