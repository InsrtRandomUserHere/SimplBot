import discord
from discord.ext import commands
import datetime


embedColor = discord.Colour.from_rgb(107, 37, 249)


class UtilityCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, *, amount=5):

        if amount == 1:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(
                f'Cleared {amount} message for {ctx.message.author.mention}!', delete_after=1.5)


        elif amount == 69:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(
                f'Cleared **noice number** messages for {ctx.message.author.mention}!', delete_after=1.5)


        else:

            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(
                f'Cleared {amount} messages for {ctx.message.author.mention}!', delete_after=1.5)

    @commands.command(aliases=['y/n'])
    async def yn(self, ctx, *, question):
        embed = discord.Embed(title="Yes/No Poll", description=question, color=embedColor, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f"Question by: {ctx.message.author.name}")

        await ctx.channel.purge(limit=1)
        m = await ctx.send(embed=embed)

        await m.add_reaction('✅')
        await m.add_reaction('❌')

    @commands.command()
    async def invite(self, ctx):
        em = discord.Embed(colour=embedColor)
        em.add_field(
            name='Invite me!',
            value='[Invite me by clicking this link](https://discord.com/api/oauth2/authorize?client_id=759052573884809246&permissions=388182&scope=bot)')
        await ctx.send(embed=em)

    @commands.command(aliases=["Guildcount", "GuildCount", "GUILDCOUNT"])
    async def guildcount(self, ctx):
        try:
            embed = discord.Embed(
                description=f"I am currently on **{len(self.client.guilds)}** servers!",
                color=embedColor)
            await ctx.send(embed=embed)

        except:
            await ctx.send(f"I am currently on **{len(self.client.guilds)}** servers!")

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(
            description=
            '[Join our support server by clicking this](https://discord.gg/2KJAJTgEZF)',
            color=embedColor
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def report(self, ctx, *, issue):
        reportchannel = self.client.get_channel(767274173658562600)

        embed = discord.Embed(
            colour=discord.Colour.blurple(), title='Issue Report')

        embed.add_field(name='Issue:', value=f'{issue}')
        embed.add_field(name='Reported by:', value=ctx.message.author.mention)

        embed2 = discord.Embed(
            description='Your report has been sent successfully!')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed2)
        await reportchannel.send(embed=embed)

    @commands.command(aliases=["InsrtsTestCommand"], case_insensitive=True)
    async def test(self, ctx):
        embed = discord.Embed(title="Test Embed",
                              description="If you are seeing this, this means that the bot is working properly")

        await ctx.send(embed=embed)
        await ctx.send("Test Message. This also means that the bot is working properly")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=f'None given'):
        embed = discord.Embed(title="User Kicked", color=discord.Color.from_rgb(0, 76, 255), timestamp=datetime.datetime.utcnow())

        embed.add_field(name='User:', value=member)
        embed.add_field(name="Kicked by:", value=ctx.message.author.mention)
        embed.add_field(name="Reason:", value=reason, inline=False)

        await member.kick(reason=f"{reason} - By: {ctx.message.author}")
        try:
        	await member.send(f"You have been **Kicked** from **{ctx.message.guild}**\n\nReason: {reason}")

        finally:
        	await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='None given'):
        embed = discord.Embed(title="User Banned", color=discord.Color.from_rgb(255, 0, 17), timestamp=datetime.datetime.utcnow())

        embed.add_field(name='User:', value=member)
        embed.add_field(name="Banned by:", value=ctx.message.author.mention)
        embed.add_field(name="Reason:", value=reason, inline=False)

        await member.ban(reason=f"{reason} - By: {ctx.message.author}")
        try:
        	await member.send(f"You have been **Banned** from **{ctx.message.guild}**\n\nReason: {reason}")

        finally:
        	await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        embed = discord.Embed(title="Slowmode Set", description=f"Set the slowmode delay in this channel to **{seconds}** seconds!", color=embedColor, timestamp=datetime.datetime.utcnow())
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(UtilityCmds(client))