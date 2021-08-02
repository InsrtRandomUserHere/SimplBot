import discord
from discord.ext import commands
import math
import random
import asyncio

embedColor = discord.Colour.from_rgb(107, 37, 249)


class GenCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', '8b'])
    async def _8ball(self, ctx):
        responses = [
            'As I see it, yes', 'Ask again later', 'Better not tell you now',
            'Cannot predict now', 'Concentrate and ask again', 'Don’t count on it',
            'It is certain', 'It is decidedly so', 'Most likely', 'My reply is no',
            'My sources say no', 'Outlook not so good', 'Outlook good',
            'Reply hazy, try again', 'Signs point to yes', 'Very doubtful',
            'Without a doubt', 'Yes', 'Yes – definitely', ' You may rely on it'
        ]
        await ctx.reply(random.choice(responses))

    @commands.command()
    async def coinflip(self, ctx):
        responses = [f'Heads!', 'Tails!']
        msg = await ctx.reply('Flipping...')
        await asyncio.sleep(0.6)
        await msg.edit(content=random.choice(responses))

    @commands.command(aliases=['calculate'])
    async def calc(self, ctx, message):
        if '+' in message or '-' in message or '/' in message or '*' in message:
            ms = eval(message)
            mbed = discord.Embed(
                title="Calculator",
                description=f"{ms}",
                colour=embedColor)

            await ctx.send(embed=mbed)
        elif "sqrt" in message:
            ma = message.replace("sqrt", "")
            await ctx.send(math.sqrt(ma))


def setup(client):
    client.add_cog(GenCmds(client))
