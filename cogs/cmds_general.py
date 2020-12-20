import discord
from discord.ext import commands
import math
import random
import asyncio
import praw
import wikipedia

embedColor = discord.Colour.from_rgb(107, 37, 249)
reddit = praw.Reddit(
    client_id='3GX8CbOHEm6h4A',
    client_secret='pFL2Iixqbd8O1yu_2KqpYvEDp14',
    username='InsrtBotUsage',
    password='discord.py',
    user_agent='pythonpraw')


class GenCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title=f"{round(self.client.latency * 1000)} ms", color=embedColor)
        await ctx.send(embed=embed)

    @commands.command(aliases=['8ball', '8b'])
    async def _8ball(self, ctx, *, question):
        responses = [
            'As I see it, yes', 'Ask again later', 'Better not tell you now',
            'Cannot predict now', 'Concentrate and ask again', 'Don’t count on it',
            'It is certain', 'It is decidedly so', 'Most likely', 'My reply is no',
            'My sources say no', 'Outlook not so good', 'Outlook good',
            'Reply hazy, try again', 'Signs point to yes', 'Very doubtful',
            'Without a doubt', 'Yes', 'Yes – definitely', ' You may rely on it'
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def membercount(self, ctx):
        i = 0
        for j in ctx.guild.members:
            i = i + 1
        embed = discord.Embed(
            title="Member count",
            description=f"There are {i} members in this server!",
            colour=embedColor)
        await ctx.send(embed=embed)

    @commands.command()
    async def coinflip(self, ctx):
        responses = [f'Heads!', 'Tails!']
        msg = await ctx.send('Flipping...')
        await asyncio.sleep(0.6)
        await msg.edit(content=f'{random.choice(responses)}')

    @commands.command(aliases=['st'])
    async def showerthought(self, ctx):
        subreddit = reddit.subreddit('showerthoughts')
        all_subs = []

        hot = subreddit.hot(limit=250)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(description=f"[**{name}**]({url})", colour=discord.Colour.blue())

        message_ = await ctx.send(embed=em)
        await message_.add_reaction('<:upvote:765210506494607420>')
        await message_.add_reaction('<:downvote:765210534613352458>')

    @commands.command()
    async def chat(self, ctx, *, message):
        embed = discord.Embed(description=message, color=embedColor)
        embed.set_footer(text=f'Message by: {ctx.message.author.name}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['calculate'])
    async def calc(self, ctx, message):
        if '+' in message or '-' in message or '/' in message or '*' in message:
            ms = eval(message)
            mbed = discord.Embed(
                title="Calculator",
                description=f"The answer is: {ms}",
                colour=embedColor)

            await ctx.send(embed=mbed)
        elif "sqrt" in message:
            ma = message.replace("sqrt", "")
            await ctx.send(math.sqrt(ma))



def setup(client):
    client.add_cog(GenCmds(client))