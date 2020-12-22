import discord
from discord.ext import commands
from pyfiglet import Figlet

embedColor = discord.Colour.from_rgb(107, 37, 249)


class TextFilter(commands.Cog):
    def __init__(self, client):
        self.client = client

    def print_cool1(self, text):
        cool_text = Figlet(font='slant')
        return str(cool_text.renderText(text))

    def print_cool3(self, text):
        cool_text = Figlet(font="3-d")
        return str(cool_text.renderText(text))

    def print_cool4(self, text):
        cool_text = Figlet(font="3x5")
        return str(cool_text.renderText(text))

    def print_cool5(self, text):
        cool_text = Figlet(font="alligator")
        return str(cool_text.renderText(text))

    def print_cool6(self, text):
        cool_text = Figlet(font="dotmatrix")
        return str(cool_text.renderText(text))

    def print_cool7(self, text):
        cool_text = Figlet(font="bubble")
        return str(cool_text.renderText(text))

    def print_cool8(self, text):
        cool_text = Figlet(font="digital")
        return str(cool_text.renderTexttext)

    @commands.command()
    async def slant(self, ctx, *, word):
        fontoutput = self.print_cool1(word)
        await ctx.channel.purge(limit=1)
        await ctx.send(
            f'```\n{fontoutput}\n\nBy: @{ctx.message.author.name}```')

    @commands.command(aliases=['3d'])
    async def _3d(self, ctx, *, word):
        fontoutput = self.print_cool3(word)
        await ctx.channel.purge(limit=1)
        await ctx.send(
            f'```\n{fontoutput}\n\nBy: @{ctx.message.author.name}```')

    @commands.command()
    async def hashtag(self, ctx, *, word):
        fontoutput = self.print_cool4(word)
        await ctx.channel.purge(limit=1)
        await ctx.send(
            f'```\n{fontoutput}\n\nBy: @{ctx.message.author.name}```')

    @commands.command()
    async def fade(self, ctx, *, word):
        fontoutput = self.print_cool5(word)
        await ctx.channel.purge(limit=1)
        await ctx.send(
            f'```\n{fontoutput}\n\nBy: @{ctx.message.author.name}```')

    @commands.command()
    async def dot(self, ctx, *, word):
        fontoutput = self.print_cool6(word)
        await ctx.channel.purge(limit=1)
        await ctx.send(
            f'```\n{fontoutput}\n\nBy: @{ctx.message.author.name}```')

    @commands.command()
    async def bubble(self, ctx, *, word):
        fontoutput = self.print_cool7(word)
        await ctx.channel.purge(limit=1)
        await ctx.send(
            f'```\n{fontoutput}\n\nBy: @{ctx.message.author.name}```')

    @commands.command()
    async def digital(self, ctx, *, word):
        fontoutput = self.self.print_cool8(word)
        await ctx.channel.purge(limit=1)
        await ctx.send(
            f'```\n{fontoutput}\n\nBy: @{ctx.message.author.name}```')


def setup(client):
    client.add_cog(TextFilter(client))
import discord
from discord.ext import commands
from pyfiglet import Figlet


embedColor = discord.Colour.from_rgb(107, 37, 249)
