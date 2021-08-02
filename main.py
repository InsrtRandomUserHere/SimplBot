import asyncio
import discord
import os
import keep_alive
from datetime import datetime
from discord.ext import commands

embedColor = discord.Colour.from_rgb(107, 37, 249)
intents = discord.Intents.default()
client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or("sb/", "Sb/", "sB/", "SB/"),
                                 intents=discord.Intents.all(), case_insensitive=True)

client.load_extension('jishaku')
client.launch_time = datetime.utcnow()
client.remove_command('help')


# Cogs (Owner Only)
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


# Owner Help Menu
@client.command()
@commands.is_owner()
async def help2(ctx):
    embed = discord.Embed(title="Owner Help Menu", colour=embedColor)
    embed.add_field(name="Cog File Names", value="```cmd_help.py\ncmds_general.py\ncmds_stats.py\ncmds_text.py"
                                                 "\ncmds_utility.py\ngenerals.py``` ")
    embed.add_field(name="Commands", value="```load <CogFile>\nunload <CogFile>\nreload <CogFile>```")
    await ctx.send(embed=embed)


# Shutdown command
@client.command(name="shutdown")
@commands.is_owner()
async def shutdownee(ctx):
    await ctx.send("Now shutting down")
    offlinelog = client.get_channel(790619786672734249)
    await offlinelog.send("🔴 Shutting down by command")
    await client.logout()


# Leave command MOVE TO UTILITY
@client.command()
@commands.has_permissions(kick_members=True)
async def leave(ctx):
    await ctx.send("Leaving Server")
    await ctx.guild.leave()


@client.command()
@commands.is_owner()
async def commandcount(ctx):
    commandsTotal = len(client.commands)
    await ctx.send(f"{commandsTotal} commands!")


# Command Error Handlers
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.purge(limit=1)
        await ctx.send("Please complete your command")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)

    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "Yeah, no. That command doesn't exist *yet*. If you want to make a command suggestion, do `sb/suggest`")

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permissions to do that")

    elif isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
        _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
        await ctx.send(_message)
        return

    elif isinstance(error, commands.NotOwner):
        await ctx.send('You are not the owner. Only InsrtRandomUserHere#0001 can use this command')

    elif isinstance(error, commands.NSFWChannelRequired):
        await ctx.send(
            'This channel is not marked as NSFW. This command can only be used in a channel that is marked as NSFW')

    elif isinstance(error, commands.MemberNotFound):
        await ctx.send('I can\'t find that user :/')

    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="You are on cooldown!",
                              description=f"Woah! Slow down there pal! You're using this command too fast! Try this "
                                          f"command again in **{error.retry_after:,.2f}** seconds",
                              color=embedColor)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error",
                              description="Oh no! An error has occurred while trying to do this command. You can use "
                                          "the `sb/report` command to report this error. If you do report this bug, "
                                          "also please include this:```{}```".format(error), color=embedColor)
        embed.set_thumbnail(url="https://assets.stickpng.com/images/5a81af7d9123fa7bcc9b0793.png")
        await ctx.send(embed=embed)


@client.command()
async def credits(ctx):
    embed = discord.Embed(title="Simple Bot Credits", color=embedColor)
    embed.add_field(name="Main Developer/Creator", value="InsrtRandomUserHere#4562", inline=False)
    embed.add_field(name="Icon Creators:",
                    value="Pythex#0001 - Normal Icon <:SimpleBot:772643241304260618>\nbean#4066 - Halloween Version "
                          "<:SpookyBot:772621287729659984>")
    embed.add_field(name="Command Ideas:", value="ItzHatsu#2515 (Shoot command)")

    await ctx.send(embed=embed)


@client.command(name="eval")
@commands.is_owner()
async def evl(ctx, *, mes):
    await ctx.send(eval(mes))


@client.command(name="UpdateLog")
async def update_log(ctx):
    embed = discord.Embed(
        description="""
```diff
Simple Bot Update Log!
Last updated: June 23. 2021
Version: 1.12.9

+Added Commands:
+RR (Go try it)
+Rate
+Would you rather (sb/wyr)
+Truth or dare (sb/tod)
+Math
+Math Score (sb/score)

-Removed Commands:
-Link Shortener
-Vote
-Owo (Don't ask)
```    """, color=embedColor)

    await ctx.send(embed=embed)


keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)
