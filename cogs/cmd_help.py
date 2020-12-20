import discord
from discord.ext import commands
import json
import datetime

embedColor = discord.Colour.from_rgb(107, 37, 249)

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    @commands.group(aliases=['help'], case_insensitive=True)
    async def _help(self, ctx):
        if ctx.invoked_subcommand is None:
            
                embed = discord.Embed(
                    title='Simple Bot Help Menu!', colour=embedColor, timestamp=datetime.datetime.utcnow())

                embed.add_field(
                    name='» General «',
                    value='`ping`, `membercount`, `calculate`', inline=False)

                embed.add_field(name="» Fun «",
                                value="`8b`, `coinflip`, `chat`, `y/n`, `hack`\n`slant`, `3d`, `hashtag`, `fade`, `dot`, `bubble`, `mirror` « Text Commands",
                                inline=False)

                embed.add_field(name="» Image «",
                                value="`wendys`, `logic`",
                                inline=False)

                embed.add_field(name="» Utility «",
                                value="`invite`, `guildcount`, `support`, `report`, `snipe`, `remind`",
                                inline=False)

                embed.add_field(name="» Moderation «",
                                value="`ban`, `kick`, `clear`, `slowmode`",
                                inline=False)

								

                embed.add_field(name="» Stats «", value="`userinfo`, `serverstats`, `channelstats`, `stats`",
                                inline=False)
                embed.set_footer(text=f'Send: sb/help <command>')

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def ping(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Ping', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Sends your ping in milliseconds',
                    inline=False)
                embed.add_field(name='Command:', value=f'```sb/ping```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def membercount(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Member count', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Sends the amount of members in the server',
                    inline=False)
                embed.add_field(name='Command:', value=f'```sb/membercount```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def calculate(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Calculate', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Calculates the equation that you send',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/calc <equation>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(aliases=['8b'], case_insensitive=True)
    async def _8b(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='8 Ball', colour=embedColor)

                embed.add_field(
                    name='Info:', value='Sends an 8ball answer', inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/8b <question>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def coinflip(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Coin flip', colour=embedColor)

                embed.add_field(name='Info:', value='Flips a coin', inline=False)
                embed.add_field(name='Command:', value=f'```sb/coinflip```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def chat(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Chat', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Make the bot send any message that you want',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/chat <message>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def clear(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Clear', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Clears an amount of messages that you want',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/clear <amount>```', inline=False)
                embed.add_field(
                    name='Note:',
                    value=
                    'You need to have the `manage messages` permission to do this command'
                )

                await ctx.send(embed=embed)

    @_help.command(aliases=['y/n'], case_insensitive=True)
    async def yn(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Yes or No', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Makes your question a yes or no poll',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/y/n <question>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def invite(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Invite', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value=
                    'Sends an invite link of me so you can invite me to your server!',
                    inline=False)
                embed.add_field(name='Command:', value=f'```sb/invite```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def guildcount(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Server Count', colour=embedColor)

                embed.add_field(
                    name='Info:', value="Sends how many servers I'm in", inline=False)
                embed.add_field(name='Command:', value=f'```sb/guildcount```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def support(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Support Server', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Sends Simple Bot's Support Server",
                    inline=False)
                embed.add_field(name='Command:', value=f'```sb/support```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def report(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Report', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Reports a bug about the bot and sends it to our support server',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/report <bug>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def kick(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Kick', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Kicks a user',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/kick <user> <reason>```', inline=False)
                embed.add_field(
                    name='Note:',
                    value=
                    'You need to have the `Kick Members` permission to do this command'
                )

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def ban(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='ban', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Bans a user',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/ban <user> <reason>```', inline=False)
                embed.add_field(
                    name='Note:',
                    value=
                    'You need to have the `Ban Members` permission to do this command'
                )

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def userinfo(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='User Info', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Shows a user's info",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/userinfo <user>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def serverstats(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Server Stats', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Shows the server's stats",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/serverstats```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def channelstats(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Channel Stats', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Shows the channel's stats",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/channelstats```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def stats(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Bot Stats', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Shows the bot's stats and info",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/stats```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def slant(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Slant', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Makes your text slanted',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/slant <text>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True, aliases=['3d'])
    async def _3d(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='3D', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Makes your text have a 3D effect',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/3d <text>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def hastag(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Hashtag', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Makes your text into a tagged effect.',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/hashtag <text>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def fade(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Fade', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Makes your text into a fading effect.',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/fade <text>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def dot(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Dot', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Makes your text into a dotted effect.',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/dot <text>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def bubble(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Bubble', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Puts your text in a bubble effect.',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/bubble <text>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def digital(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Digital', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value='Puts your text in a digital effect.',
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/digital <text>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def setprefix(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Set Prefix', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Changes the bot's prefix in this server",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/setprefix <prefix>```', inline=False)
                embed.add_field(
                    name='Note:', value=f'You need to be an administrator to use this command', inline=False)
                embed.add_field(
                    name='Aliases:', value=f'`changeprefix`, `set_prefix`', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def slowmode(self, ctx):
        if ctx.invoked_subcommand is None:
            
                

                
                embed = discord.Embed(
                    title='Set Slowmode', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Changes the current channel's slowmode",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/slowmode <seconds>```', inline=False)
                embed.add_field(
                    name='Note:', value=f'You need to have the `Manage Messages` permission to use this command', inline=False)
			

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def snipe(self, ctx):
        if ctx.invoked_subcommand is None:

                embed = discord.Embed(
                    title='Snipe', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Sends the last deleted messsage in the current channel",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/snipe```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def mirror(self, ctx):
        if ctx.invoked_subcommand is None:

                embed = discord.Embed(
                    title='Mirror', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Mirrors your text",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/mirror <phrase>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def hack(self, ctx):
        if ctx.invoked_subcommand is None:

                embed = discord.Embed(
                    title='Hack', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="**Tries** to hack the user you mention\n||Don't worry, we're not actually hacking someone. This is just for fun||",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/hack <member>```', inline=False)

                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def wendys(self, ctx):
        if ctx.invoked_subcommand is None:

                embed = discord.Embed(
                    title='Sir, This is a Wendy\'s', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Puts your thought in the \"Sir, this is a Wendy's\" Meme",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/wendys <thought>```', inline=False)
                embed.set_image(
                    url="https://preview.redd.it/hebnnjrr53h41.jpg?auto=webp&s=12c85c1862c21e422d762a7b6507f4510b5cff10")
                await ctx.send(embed=embed)

    @_help.command(case_insensitive=True)
    async def logic(self, ctx):
        if ctx.invoked_subcommand is None:

                embed = discord.Embed(
                    title='Intense Logic Thinking', colour=embedColor)

                embed.add_field(
                    name='Info:',
                    value="Wonder what their logic is",
                    inline=False)
                embed.add_field(
                    name='Command:', value=f'```sb/logic <NotALogic>```', inline=False)
                embed.set_image(
                    url="https://i0.wp.com/boingboing.net/wp-content/uploads/2016/11/bcf.png?fit=680%2C445&ssl=1")

                await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Help(client))