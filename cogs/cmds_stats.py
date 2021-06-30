import discord
from discord.ext import commands
import datetime

embedColor = discord.Colour.from_rgb(107, 37, 249)
lastUpdate = "February 4 2021"
version = "1.12.9"
"""Version Guide:
Major build number: This indicates a major milestone in the game, increment this when going from beta to release, from release to major updates.

Minor build number: Used for feature updates, large bug fixes etc.

Revision: Minor alterations on existing features, small bug fixes, etc. 
"""
API = "<:API:789895339002953769>"
ID = "<:IDCard:789879740450078741>"
Uptime = "<:uptime:789888461086916648>"
User = "<:user:789885278621925447>"
Downlaod = "<:Downlaod:789880705328873482>"
Upload = "<:upload:789890027487232000>"
Crown = "<:Crown:789881455655518328>"
Versions = "<:Versions:789890650173865985>"
API = "<:API:789895339002953769>"
Server = "<:Server:789898001791320084>"


class Stats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author

        roles = [role for role in member.roles]
        user = ctx.message.author
        hype = [i[0].replace("_", " ").title() for i in user.public_flags
                if i[1] and "hypesquad" in i[0]]



        embed = discord.Embed(colour=embedColor, timestamp=datetime.datetime.utcnow())

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text=f'Requested by {ctx.author}\n', icon_url=ctx.author.avatar_url)

        embed.add_field(name='UserID:', value=member.id, inline=True)
        embed.add_field(
            name=f'Account Created at:\n(YYYY/MM/DD)',
            value=member.created_at.date(),
            inline=True)
        embed.add_field(
            name='Nickname in server:', value=member.display_name, inline=False)

        embed.add_field(name='Status: (Desktop)', value=str(member.desktop_status).replace("dnd", "Do not disturb"))
        embed.add_field(name='Status: (Mobile App)', value=str(member.mobile_status).replace("dnd", "Do not disturb"))
        embed.add_field(name='Status: (Website)', value=str(member.web_status).replace("dnd", "Do not disturb"))

        embed.add_field(
            name='Animated Avatar?:', value=str(member.is_avatar_animated()).replace("False", "No").replace("True", "Yes"), inline=False)

        embed.add_field(
            name=f'Roles ({len(roles)})',
            value=''.join([role.mention for role in roles]))
        embed.add_field(name='Top role:', value=member.top_role.mention, inline=False)

        embed.add_field(
            name='Joined this server at:', value=member.joined_at.date(), inline=False)

        embed.add_field(name='Bot?', value=str(member.bot).replace("False", "No").replace("True", "Yes"), inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['channelinfo'])
    async def channelstats(self, ctx):
        channel = ctx.channel

        embed = discord.Embed(
            title=f"Stats for **{channel.name}**",
            description=
            f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}",
            colour=embedColor, timestamp=datetime.datetime.utcnow())

        embed.add_field(name="Channel Id", value=channel.id)
        embed.add_field(
            name="Topic:",
            value=f"{channel.topic if channel.topic else 'No topic.'}")
        embed.add_field(name="Position:", value=channel.position)
        embed.add_field(name="Slowmode Delay:", value=channel.slowmode_delay)
        embed.add_field(name="nsfw?:", value=channel.is_nsfw())
        embed.add_field(name="news?:", value=channel.is_news())
        embed.add_field(
            name="Creation Time:\n(YYYY-MM-DD)", value=channel.created_at.date())

        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx):
        embed = discord.Embed(title="Bot Stats", color=embedColor)
    
        delta_uptime = datetime.datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
    
        embed.add_field(name=f"{ID} Username:", value="Simple Bot#5958")
        embed.add_field(name=f"{ID} User ID:", value="759052573884809246", inline=False)
        embed.add_field(name=f"{Upload} API Ping:", value=f"{round(self.client.latency * 1000)}ms", inline=False)
        embed.add_field(name=f"{Uptime} Uptime:",
                        value=f"`{days}` Day(s)\n`{hours}` Hour(s)\n`{minutes}` Minute(s)\n`{seconds}` Seconds")
        embed.add_field(name=f"{Versions} Version:", value=version, inline=False)
        embed.add_field(name=f"{Server} Servers:", value=f"{len(self.client.guilds)} Servers", inline=False)
        embed.add_field(name=f"{User} Users:", value=f"{len(self.client.users)} Users")
    
        embed.add_field(name=f"{Downlaod} Last Updated:", value=lastUpdate, inline=False)
        embed.add_field(name=f"{Crown} Owner/Creator:", value="InsrtRandomUserHere#4562", inline=False)
        embed.add_field(name=f"{API} API/Library:", value=f"discord.py {discord.__version__}", inline=False)
    
    
    
        await ctx.send(embed=embed)
    
    """Version Guide:
    Major build number: This indicates a major milestone in the game, increment this when going from beta to release, from release to major updates.
    
    Minor build number: Used for feature updates, large bug fixes etc.
    
    Revision: Minor alterations on existing features, small bug fixes, etc. 
    """

    @commands.command(aliases=['serverinfo'])
    async def serverstats(self, ctx):
        g = ctx.guild

        embed = discord.Embed(
            title=f'Server Info: {g.name}', colour=embedColor, timestamp=datetime.datetime.utcnow())

        total_text_channels = len(g.text_channels)
        total_voice_channels = len(g.voice_channels)
        total_channels = total_text_channels + total_voice_channels


        embed.add_field(name='Name:', value=g.name)
        embed.add_field(name='Region:', value=g.region)
        embed.add_field(name='Server ID:', value=g.id)

        embed.add_field(name='Description:', value=g.description)
        embed.add_field(name='Verification Level:', value=g.verification_level)

        embed.add_field(name='Boost Level:', value=g.premium_tier)
        embed.add_field(name='Amount of Boosts:', value=g.premium_subscription_count)
        embed.add_field(name='Emoji Limit:', value=g.emoji_limit)

        embed.add_field(name='Owner:', value=g.owner.mention)
        embed.add_field(name="Text Channels: ", value=total_text_channels)
        embed.add_field(name="Voice Channels: ", value=total_voice_channels)
        embed.add_field(name="Total Channels:", value=total_channels)

        embed.add_field(name="Total Members:", value=f"{len(g.members)}")
        embed.add_field(name="Bots:", value=f"{len(g.members.bot)}")
        embed.add_field(name="Users:", value=f"{len([m for m in ctx.guild.members if not m.bot])}")

        embed.add_field(
            name='Created at:\n(YYYY-MM-DD)', value=g.created_at.date())

        embed.set_thumbnail(url=g.icon_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Stats(client))