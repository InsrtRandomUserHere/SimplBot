import keep_alive
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import os
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext
from datetime import datetime
import random



#Just importing some modules



embedColor = discord.Colour.from_rgb(107, 37, 249)
#The color for embeds

intents = discord.Intents.default()



client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or("sb/", "Sb/", "sB/", "SB/"), intents=discord.Intents.all(), case_insensitive=True)
slash = SlashCommand(client)

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
    offlinelog = client.get_channel(790619786672734249)
    await offlinelog.send("🔴 Shutting down by command")
    await client.logout()

@client.command()
@commands.is_owner()
async def char(ctx, *, x):
	await ctx.send(len(x))

@client.command()
async def owo(ctx, *, phrase):
	await ctx.send(phrase.replace("l", "w"))

@client.command()
async def vote(ctx):
	embed = discord.Embed(title="Vote for me on some websites!",
		description="[Vote for me on Top.gg here](https://top.gg/bot/759052573884809246/vote)\n"
		"[Vote for me on DiscordBotList!](https://discordbotlist.com/bots/simple-bot/upvote)\n",
		color=embedColor
	)
	await ctx.send(embed=embed)

@client.command()
async def commandcount(ctx):
	commandsTotal = len(client.commands)
	await ctx.send(f"{commandsTotal} commands!")

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

@client.command()
async def credits(ctx):
	embed = discord.Embed(title="Simple Bot Credits", color=embedColor)
	embed.add_field(name="Icon Creators:", value="Pythex#0001 - Normal Icon <:SimpleBot:772643241304260618>\nbean#4066 - Halloween Version <:SpookyBot:772621287729659984>")
	embed.add_field(name="Command Ideas:", value="ItzHatsu#2515")
	embed.add_field(name="Quotes Source:", value="[braintancy](https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/)")
	await ctx.send(embed=embed)

@client.command()
async def quote(ctx):
	quotes = [
		"“The Best Way To Get Started Is To Quit Talking And Begin Doing.”\n\n– Walt Disney",
		"“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.”\n\n– Winston Churchill",
		"“Don’t Let Yesterday Take Up Too Much Of Today.”\n\n– Will Rogers",
		"“You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.”\n\n– Unknown",
		"“It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.”\n\n– Vince Lombardi"
	]
	await ctx.send(random.choice(quotes))




@client.command(name="eval")
@commands.is_owner()
async def evl(ctx, *, mes):
	await ctx.send(eval(mes))

@client.command(aliases=["av", "pfp"])
async def avatar(ctx, *, member:discord.Member=None):
	if member == None:
		embed = discord.Embed(title=f"{ctx.author}'s Avatar", color=embedColor)
		embed.set_image(url=ctx.author.avatar_url)

	else:
		embed = discord.Embed(title=f"{member}'s Avatar", color=embedColor)
		embed.set_image(url=member.avatar_url)

	await ctx.reply(embed=embed)


#Main Brain
keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)