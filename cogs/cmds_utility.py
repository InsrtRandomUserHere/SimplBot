import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import datetime
import asyncio


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

    @commands.command(aliases=['y/n', 'poll'])
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
            value='[Invite me by clicking this link](https://discord.com/api/oauth2/authorize?client_id=759052573884809246&permissions=388182&scope=bot)\n[Click this one if you want slash commands!](https://discord.com/oauth2/authorize?client_id=759052573884809246&permissions=388182&scope=applications.commands%20bot)')
        await ctx.send(embed=em)

    @commands.command()
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

    @commands.command()
    @commands.cooldown(1, 600, BucketType.user)
    async def suggest(self, ctx, *, suggestion):
        reportchannel = self.client.get_channel(806586944767000626)

        embed = discord.Embed(
            colour=embedColor, title='Suggestion')

        embed.add_field(name='Suggestion:', value=f'{suggestion}')
        embed.add_field(name='Requested by:', value=ctx.message.author.mention)


        embed2 = discord.Embed(
            description='Your suggestion has been sent successfully!', color=embedColor)
        x = await reportchannel.send(embed=embed)
        e = await ctx.send(embed=embed2)

        await x.add_reaction("⬆️")
        await x.add_reaction("⬇️")

        embed2 = discord.Embed(
            description='Your suggestion has been sent successfully!')


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
        embed.add_field(name="Kicked by:", value=ctx.author.mention)
        embed.add_field(name="Reason:", value=reason, inline=False)

        await member.kick(reason=f"{reason} - By: {ctx.message.author}")
        try:
            kick_embed = discord.Embed(title=f"You have been kicked from {ctx.message.guild}", color=discord.Colour.gold())
            kick_embed.add_field(name="Reason", value=reason)
            await member.send(embed=kick_embed)

        finally:
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='None given'):
        embed = discord.Embed(title="User Banned", color=discord.Color.from_rgb(255, 0, 17), timestamp=datetime.datetime.utcnow())

        embed.add_field(name='User:', value=member)
        embed.add_field(name="Banned by:", value=ctx.author.mention)
        embed.add_field(name="Reason:", value=reason, inline=False)

        await member.ban(reason=f"{reason} - By: {ctx.message.author}")
        try:
            ban_embed = discord.Embed(title=f"You have been banned from {ctx.message.guild}", colour=discord.Colour.red())
            ban_embed.add_field(name='Reason', value=reason)
            await member.send(embed=ban_embed)

        finally:
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        embed = discord.Embed(title="Slowmode Set", description=f"Set the slowmode delay in this channel to **{seconds}** seconds!", color=embedColor, timestamp=datetime.datetime.utcnow())
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(embed=embed)

    @commands.command(case_insensitive=True, aliases=["remind", "remindme", "remind_me"])
    @commands.bot_has_permissions(attach_files=True, embed_links=True)
    async def reminder(self, ctx, time, *, reminder):
        print(time)
        print(reminder)
        user = ctx.message.author
        embed = discord.Embed(color=embedColor, timestamp=datetime.datetime.utcnow())
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
            embed.add_field(name='Warning',
                            value='You have specified a too long duration!\nMaximum duration is 90 days.')
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

    @commands.command(aliases=["av", "pfp"])
    @commands.cooldown(1, 3, BucketType.user)
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            embed = discord.Embed(title=f"{ctx.author}'s Avatar", color=embedColor)
            embed.set_image(url=ctx.author.avatar_url)

        else:
            embed = discord.Embed(title=f"{member}'s Avatar", color=embedColor)
            embed.set_image(url=member.avatar_url)

        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def leave(self, ctx):
        await ctx.send("Leaving Server")
        await ctx.guild.leave()


def setup(client):
    client.add_cog(UtilityCmds(client))