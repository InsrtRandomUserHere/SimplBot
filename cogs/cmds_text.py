import discord
from discord.ext import commands
from pyfiglet import Figlet

embedColor = discord.Colour.from_rgb(107, 37, 249)


class TextFilter(commands.Cog):
    def __init__(self, client):
        self.client = client

    def ascii(self, text):
        font_chosen = Figlet()
        return str(font_chosen.renderText(text))

    def ascii_slant(self, text):
        font_chosen = Figlet(font='slant')
        return str(font_chosen.renderText(text))

    def _3d(self, text):
        font_chosen = Figlet(font="3-d")
        return str(font_chosen.renderText(text))

    def tag(self, text):
        font_chosen = Figlet(font="3x5")
        return str(font_chosen.renderText(text))

    def fade(self, text):
        font_chosen = Figlet(font="alligator")
        return str(font_chosen.renderText(text))

    def dot(self, text):
        font_chosen = Figlet(font="dotmatrix")
        return str(font_chosen.renderText(text))

    def bubble(self, text):
        font_chosen = Figlet(font="bubble")
        return str(font_chosen.renderText(text))

    def digital(self, text):
        font_chosen = Figlet(font="digital")
        return str(font_chosen.renderText(text))

    @commands.command()
    async def slant(self, ctx, *, word):
        font_output = self.ascii_slant(word)
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')

    @commands.command(aliases=['3d'])
    async def _3d(self, ctx, *, word):
        font_output = self._3d(word)
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')

    @commands.command()
    async def hashtag(self, ctx, *, word):
        font_output = self.tag(word)
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')

    @commands.command()
    async def fade(self, ctx, *, word):
        font_output = self.fade(word)
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')

    @commands.command()
    async def dot(self, ctx, *, word):
        font_output = self.dot(word[:2000])
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')

    @commands.command()
    async def bubble(self, ctx, *, word):
        font_output = self.bubble(word)
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')

    @commands.command()
    async def digital(self, ctx, *, word):
        font_output = self.self.digital(word)
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')

    @commands.command()
    async def mirror(self, ctx, *, phrase):
        await ctx.reply(phrase[::-1])

    @commands.command()
    async def ascii(self, ctx, *, word):
        font_output = self.ascii(word)
        await ctx.send(
            f'```\n{font_output}\n\nBy: @{ctx.author.name}```')


def setup(client):
    client.add_cog(TextFilter(client))
