import discord
from discord.ext import commands

embedColor = discord.Colour.from_rgb(107, 37, 249)


class MiscCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def credits(self, ctx):
        embed = discord.Embed(title="Simple Bot Credits", color=embedColor)
        embed.add_field(name="Main Developer/Creator", value="InsrtRandomUserHere#4562", inline=False)
        embed.add_field(name="Icon Creators:",
                        value=f"{self.client.get_user(760662713818415104)} - Default <:SimpleBot:772643241304260618>\n"
                              f"{self.client.get_user(684671542407331872)} - Halloween <:Pumpkin:772621287729659984>\n"
                        )
        embed.add_field(name="Command Ideas:",
                        value=f"{self.client.get_user(647760649237037096)} - Shoot Command")

        await ctx.send(embed=embed)

    @commands.command(name="UpdateLog")
    async def update_log(self, ctx):
        embed = discord.Embed(
            description="""
    ```diff
    Simple Bot Update Log!
    Last updated: Aug 2 2021
    Version: 1.13.9

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
    ```""", color=embedColor)
        await ctx.send(embed)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title=f"{round(self.client.latency * 1000)} ms", color=embedColor)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(MiscCommands(client))