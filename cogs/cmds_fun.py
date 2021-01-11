import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import aiohttp
import asyncio
import random
from random import randint
import datetime

snipe_message_content = None
snipe_message_author = None
embedColor = discord.Colour.from_rgb(107, 37, 249)

class FunCmds(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        global snipe_message_content
        global snipe_message_author
        # Variables outside a function have to be declared as global in order to be changed

        snipe_message_content = message.content
        snipe_message_author = message.author
        await asyncio.sleep(60)
        snipe_message_author = None
        snipe_message_content = None


    @commands.command()
    @commands.is_owner()
    async def sub(self, ctx, *, sub):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r/{sub}/hot.json") as response:
                j = await response.json()

        data = j["data"]["children"][random.randint(0, 25)]["data"]
        image_url = data["url"]
        title = data["title"]
        em = discord.Embed(title=title, color=embedColor)
        em.set_image(url=image_url)
        em.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    async def snipe(self, message):
        if snipe_message_content == None:
            await message.channel.send("Theres nothing to snipe.")
        else:
            embed = discord.Embed(description=f"{snipe_message_content}", timestamp=datetime.datetime.utcnow(), color=embedColor)
            embed.set_author(name=f"{snipe_message_author}", icon_url=snipe_message_author.avatar_url)

            await message.channel.send(embed=embed)
            return

    @commands.command()
    @commands.is_owner()
    async def fsnipe(self, ctx, member:discord.Member, *, mes):
            await ctx.message.channel.purge(limit=1)
            embed = discord.Embed(description=f"{mes}", timestamp=datetime.datetime.utcnow(), color=embedColor)
            embed.set_author(name=f"{member}", icon_url=member.avatar_url)

            await ctx.send(embed=embed)


    @commands.command()
    async def rr(self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.author.send("https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ")

        else:
            await member.send(f"https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ")
            await member.send(f"You were rickrolled by **{ctx.message.author}**!")		

    # hack command that im too lazy to put in a cog
    # Obviously this command does not hack anybody
    @commands.command()
    @commands.cooldown(1, 15, BucketType.user)
    async def hack(self, ctx, member: discord.Member = None):
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

    @commands.command()
    async def shoot(self, ctx, *, member: discord.Member = None):
        scenarios = ["dodges", "Survived", "ShooterGetsArrested"]
        outcome = random.choice(scenarios)
        author = ctx.message.author

        if member == None:
            await ctx.send("Who are you gonna shoot?")

        if member == author:
            await ctx.send("You need to get some help man")

        if member is not None and member is not author and outcome == "dodges":
            message = await ctx.send(
                f"{author.mention} Tried to shoot {member.mention} but {member.name} managed to dodge the bullet!")

        elif member is not None and member is not author and outcome == "Survived":
            message = await ctx.send(f"Oh no! {author.mention} just shot {member.mention}!")
            await asyncio.sleep(4)
            await message.edit(
                content="But wait! What's this? **{} managed to survive the gunshot!**".format(member.mention))

        elif member is not None and member is not author and outcome == "ShooterGetsArrested":
            DeathMessage = [f"roasted", "T-Posed on", "dabbed on", "bonked", "default danced on"]
            randomDeathMessage = random.choice(DeathMessage)
            message = await ctx.send(f"{author.mention} was about to shoot {member.mention} but the police arrived!")
            await asyncio.sleep(2)
            await message.edit(
                content=f"{member.mention} **" + randomDeathMessage + f"** {author.mention} after seeing {author.mention} get arrested")
            await asyncio.sleep(3)
            await ctx.send(
                f"After being in jail for a while, {author.mention} found out that an admin of this server saw the scene and called the police")

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r/memes/hot.json") as response:
                j = await response.json()

        data = j["data"]["children"][random.randint(0, 25)]["data"]
        image_url = data["url"]
        title = data["title"]
        em = discord.Embed(title=title, color=embedColor)
        em.set_image(url=image_url)
        em.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command(aliases=["st"])
    async def showerthought(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r/showerthoughts/hot.json") as response:
                j = await response.json()

        data = j["data"]["children"][random.randint(0, 25)]["data"]
        image_url = data["url"]
        title = data["title"]
        em = discord.Embed(title=title, color=embedColor)
        em.set_image(url=image_url)
        em.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)



def setup(client):
    client.add_cog(FunCmds(client))