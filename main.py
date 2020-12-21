import keep_alive
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import os
from datetime import datetime
import reddit
import random
from random import randint
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
#Just importing some modules



embedColor = discord.Colour.from_rgb(107, 37, 249)
#The color for embeds

intents = discord.Intents.default()



client = commands.Bot(command_prefix="sb/", intents=discord.Intents.all())

#Getting uptime
client.launch_time = datetime.utcnow()

#Removing default help command
client.remove_command('help')

#Globals for snipe command
snipe_message_content = None
snipe_message_author = None



@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author
    # Variables outside a function have to be declared as global in order to be changed

    snipe_message_content = message.content
    snipe_message_author = message.author
    await asyncio.sleep(60)
    snipe_message_author = None
    snipe_message_content = None


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


#Owner only subreddit comand
@client.command()
@commands.is_owner()
async def subred(ctx, *, sub):
    subreddit = reddit.subreddit(sub)
    all_subs = []

    top = subreddit.hot(limit=250)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(
        title=name, colour=discord.Colour.from_rgb(255, 192, 203))

    em.set_image(url=url)

    await ctx.send(embed=em)

#leave command
@client.command()
@commands.has_permissions(kick_members=True)
async def leave(ctx):
    await ctx.send("Leaving Server")
    await ctx.guild.leave()

#Snipe command
@client.command()
async def snipe(message):
    if snipe_message_content == None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}", timestamp=datetime.utcnow(), color=embedColor)
        embed.set_author(name=f"{snipe_message_author}", icon_url=snipe_message_author.avatar_url)

        await message.channel.send(embed=embed)
        return

# Rickroll command
@client.command()
async def rr(ctx):
    await ctx.author.send("https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ")

#reminder command 
@client.command(case_insensitive=True, aliases=["remind", "remindme", "remind_me"])
@commands.bot_has_permissions(attach_files=True, embed_links=True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=embedColor, timestamp=datetime.utcnow())
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning',
                        value='Please specify what do you want me to remind you about.')  # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='Warning',
                        value='Please specify a proper duration, send `sb/help reminder` for more information.')
        embed.set_thumbnail(url="https://assets.stickpng.com/images/5a81af7d9123fa7bcc9b0793.png")
    elif seconds < 300:
        embed.add_field(name='Warning',
                        value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
        embed.set_thumbnail(url="https://assets.stickpng.com/images/5a81af7d9123fa7bcc9b0793.png")
    elif seconds > 7776000:
        embed.add_field(name='Warning', value='You have specified a too long duration!\nMaximum duration is 90 days.')
        embed.set_thumbnail(url="https://assets.stickpng.com/images/5a81af7d9123fa7bcc9b0793.png")
    else:
        await ctx.send(f"Alright, I will remind you about {reminder} in {counter}.")
        await asyncio.sleep(seconds)
        try:
            await ctx.message.author.send(
                f"Hi, you asked me to remind you about **{reminder}** in **{ctx.message.guild}** **{counter}** ago.")

        except:
            await ctx.send(
                f"Hey {ctx.message.author.mention}, you asked me to remind you about **{reminder}** in this server **{counter}** ago.")
        return
    await ctx.send(embed=embed)

#hack command that im too lazy to put in a cog
# Obviously this command does not hack anybody
@client.command()
@commands.cooldown(1, 15, BucketType.user)
async def hack(ctx, member: discord.Member = None):
    attempt = ["Success", "Fail"]
    guess = random.choice(attempt)
    author = ctx.message.author
    if member == None:
        await ctx.send("Who are we hacking? Mention someone to hack")

    if member == ctx.message.author:
        await ctx.send("Why are you gonna hack yourself? You can't do that 😕")

    elif member is not None and member is not author and guess == "Success":
        reverse = member.display_name
        message = await ctx.send(f"Now attempting to hack {member}...")
        await asyncio.sleep(2)
        await message.edit(content="Getting email...")
        await asyncio.sleep(2)
        await message.edit(content="Getting email complete!")
        await asyncio.sleep(1)
        await message.edit(content="Getting password...")
        await asyncio.sleep(2)
        await message.edit(content="Password guess completed")
        await asyncio.sleep(1)
        await message.edit(content="Getting IP Address...")
        await asyncio.sleep(1)
        await message.edit(content="Hack completed")
        await asyncio.sleep(1)
        await message.edit(
            content=f"{member.name}'s Info:\nEmail: ||{member.name}42d15C0rD@gmail.com||\nPassword: ||6{reverse[::-1]}9||\nIP Address: ||{randint(110, 255)}.{randint(110, 255)}.69.420||")

    elif member is not None and member is not author and guess == "Fail":
        message = await ctx.send(f"Attempting to hack {member}...")
        await asyncio.sleep(4)
        await message.edit(
            content=f"Oh, you thought this was actually gonna hack {member.name}? Nope, this was a trap all along. You have now been reported to Discord for trying to abuse the API")
        await asyncio.sleep(10)
        try:
            await ctx.message.author.send(
                "Don't worry, you're not actually reported to Discord. The hack command is just a joke")
        except:
            await ctx.send(
                f"Hey {ctx.message.author.mention}. Don't worry, you're not actually reported to Discord. The hack command is just a joke")

#Shutdown command
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Now shutting down")
    await client.logout()

#Shoot command
@client.command()
async def shoot(ctx, *, member : discord.Member=None):
	scenarios=["dodges", "Survived", "ShooterGetsArrested"]
	outcome = random.choice(scenarios)
	author = ctx.message.author

	if member == None:
		await ctx.send("Who are you gonna shoot?")

	if member == author:
		await ctx.send("You need to get some help man")

	if member is not None and member is not author and outcome == "dodges":
		message = await ctx.send(f"{author.mention} Tried to shoot {member.mention} but {member.name} managed to dodge the bullet!")
	
	elif member is not None and member is not author and outcome == "Survived":
		message = await ctx.send(f"Oh no! {author.mention} just shot {member.mention}!")
		await asyncio.sleep(4)
		await message.edit(content="But wait! What's this? **{} managed to survive the gunshot!**".format(member.mention))

	elif member is not None and member is not author and outcome == "ShooterGetsArrested":
		DeathMessage=[f"roasted", "T-Posed on", "dabbed on", "bonked", "default danced on"]
		randomDeathMessage = random.choice(DeathMessage)
		message = await ctx.send(f"{author.mention} was about to shoot {member.mention} but the police arrived!")
		await asyncio.sleep(2)
		await message.edit(content=f"{member.mention} **" + randomDeathMessage + f"** {author.mention} after seeing {author.mention} get arrested")
		await asyncio.sleep(3)
		await ctx.send(f"After being in jail for a while, {author.mention} found out that an admin of this server saw the scene and called the police")


#Image commands that im gonna put in a cog soon
@client.command()
@commands.cooldown(1, 5, BucketType.user)
async def wendys(ctx, *, thought):
	x = thought
	x = x.split()
	if len(x) <= 36:
		for i in range(len(x)):
			if i%4 == 0 and i != 0:
				x.insert(i, '\n')

		e = ' '.join(map(str, x))
		img = Image.open("wendys.jpg")
		font = ImageFont.truetype("arial.ttf", 50)
		draw = ImageDraw.Draw(img)

		draw.text((520,110), e, (0,0,0), font=font, align='center')
		img.save("sir_this_is_a_wendys.jpg")
		await ctx.send(file=discord.File("sir_this_is_a_wendys.jpg"))

	elif len(x) >= 36:
		await ctx.send("Woah, that's too much. Go under the 36 character limit")


@client.command()
@commands.cooldown(1, 5, BucketType.user)
async def logic(ctx, *, notalogic):
	x = notalogic
	x = x.split()
	if len(x) <= 36:
		for i in range(len(x)):
			if i%5 == 0 and i != 0:
				x.insert(i, '\n')

		e = ' '.join(map(str, x))
		img = Image.open("logic.png").convert("RGB")
		font = ImageFont.truetype("arial.ttf", 50)
		draw = ImageDraw.Draw(img)

		draw.text((5,10), e, (0,0,0), font=font, align='left')
		img.save("what_is_the_logic.png")
		await ctx.send(file=discord.File("what_is_the_logic.png"))

	elif len(x) >= 36:
		await ctx.send("Woah, that's too much. Go under the 36 character limit")


@client.command()
@commands.cooldown(1, 5, BucketType.user)
async def burn(ctx, *, thought):
	x = thought
	x = x.split()
	if len(x) <=36:
		for i in range(len(x)):
			if i%3 == 0 and i != 0:
				x.insert(i, '\n')
		e = ' '.join(map(str, x))
		img = Image.open("burn.jpg").convert("RGB")
		font = ImageFont.truetype("arial.ttf", 25)
		draw = ImageDraw.Draw(img)

		draw.text((70,100), e, (0,0,0), font=font, align='center')
		img.save("lets_burn_this.png")
		await ctx.send(file=discord.File("lets_burn_this.png"))

	elif len(x) >= 36:
		await ctx.send("Woah, that's too much. Go under the 36 character limit")



@client.command()
@commands.cooldown(1, 5, BucketType.user)
async def worthless(ctx, *, thing):
	x = thing
	x = x.split()
	if len(x) <= 36:
		for i in range(len(x)):
			if i%4 == 0 and i != 0:
				x.insert(i, '\n')

		e = ' '.join(map(str, x))
		img = Image.open("worthless.jpg").convert("RGB")
		font = ImageFont.truetype("arial.ttf", 25)
		draw = ImageDraw.Draw(img)

		draw.text((61,74), e, (0,0,0), font=font, align='center')
		img.save("woah_this_is_worthless.png")
		await ctx.send(file=discord.File("woah_this_is_worthless.png"))
	
	elif len(x) >= 36:
		await ctx.send("Your sentence is longer than 50 characters. Go under that limit!")

@client.command()
@commands.cooldown(1, 5, BucketType.user)
async def sleep(ctx, *, thing):
	x = thing
	x = x.split()
	if len(x) <= 36:
		for i in range(len(x)):
			if i%4 == 0 and i != 0:
				x.insert(i, '\n')

		e = ' '.join(map(str, x))
		img = Image.open("sleep.jpg").convert("RGB")
		font = ImageFont.truetype("arial.ttf", 25)
		draw = ImageDraw.Draw(img)

		draw.text((27,338), e, (0,0,0), font=font, align='center')
		img.save("are_you_going_to_sleep.png")
		await ctx.send(file=discord.File("are_you_going_to_sleep.png"))
	
	elif len(x) >= 36:
		await ctx.send("Your sentence is longer than 50 characters. Go under that limit!")

@client.command()
async def ID(ctx, user : discord.Member=None):
	if user == None:
		user = ctx.author
	
	ID = Image.open("DiscordUserIDTemplate.png")
	asset = user.avatar_url_as(size=128)
	data = BytesIO(await asset.read())
	pfp = Image.open(data)
	pfp = pfp.resize((264,264))
	font = ImageFont.truetype("arlrdbd.ttf", 40)
	draw = ImageDraw.Draw(ID)

	draw.text((313,135), user.name, (255,255,255), font=font, align='left')
	draw.text((313,240), user.discriminator, (255,255,255), font=font, align='left')
	draw.text((313,355), str(user.id), (255,255,255), font=font, align='left')
	draw.text((313,468), str(user.created_at.date()), (255,255,255), font=font, align='left')
	ID.paste(pfp, (17,102))
	ID.save("MemberID.png")
	await ctx.send(file=discord.File("MemberID.png"))




# @client.event stuff------------------------------------------------------------------------------------------

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