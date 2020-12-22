import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import json
from random import randint
import random

embedColor = discord.Colour.from_rgb(107, 37, 249)

class economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def open_account(self, user):
        with open("json_files/mainbank.json", "r") as f:
            users = json.load(f)

        if str(user.id) in users:
            return False

        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 100
            users[str(user.id)]["wallet"] = 0

        with open("json_files/mainbank.json", "w") as f:
            json.dump(users,f)
        return True

    async def get_bank_data(self):
        with open("json_files/mainbank.json", "r") as f:
            users = json.load(f)

        return users

    async def add_to_bank_data(self, users):
        with open("json_files/mainbank.json", "w") as f:
            json.dump(users,f)


    @commands.command(aliases=["bal"])
    async def balance(self, ctx, member:discord.Member=None):
        users = await self.get_bank_data()
        wallet_amt = users[str(self.user.id)][self.wallet]
        bank_amt = users[str(self.user.id)][self.bank]

        if member == None:
            user = ctx.author
            await self.open_account(user)


            em = discord.Embed(title=f"{user.display_name}'s Balance", color=embedColor)
            em.add_field(name="Wallet:", value=wallet_amt)
            em.add_field(name="Bank:", value=bank_amt)
            await ctx.send(embed=em)

        else:
            await self.open_account(member)
            em = discord.Embed(title=f"{member.display_name}'s Balance", color=embedColor)
            em.add_field(name="Wallet:", value=wallet_amt)
            em.add_field(name="Bank:", value=bank_amt)
            await ctx.send(embed=em)

    @commands.command()
    async def beg(self, ctx):
        users = await self.get_bank_data()
        user = ctx.author
        await self.open_account(user)



        answer = random.choice(['yes', 'no'])
        person = random.choice(['PewDiePie', 'Felix Kjellberg', 'MrBeast'])
        earnings = randint(0, 101)

        if answer == 'yes':
            await ctx.send(f"{person} has gave you {earnings}")
            users[str(user.id)][self.wallet] += earnings
            await self.add_to_bank_data()

        wallet_amt = users[str(user.id)][self.wallet]








        

def setup(client):
	client.add_cog(economy(client)) 