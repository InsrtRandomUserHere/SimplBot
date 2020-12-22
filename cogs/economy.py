import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import json
from random import randint
import random

embedColor = discord.Colour.from_rgb(107, 37, 249)

class economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def open_account(self, user):
        users = await self.get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]['wallet'] = 0
            users[str(user.id)]['bank'] = 0

        with open('./data/mainbank.json', 'w') as f:
            json.dump(users, f)
        return True


    async def get_bank_data(self):
        with open('./data/mainbank.json', 'r') as f:
            users = json.load(f)

        return users


    async def update_bank(self, user, change = 0,mode='wallet'):
        users = await self.get_bank_data()

        users[str(user.id)][mode] += change

        with open('./data/mainbank.json', 'w') as f:
            json.dump(users, f)

        bal = [users[str(user.id)]['wallet'], users[str(user.id)]['bank']]
        return bal

    @commands.command(aliases=['bal'])
    @cooldown(1, 3, BucketType.user)
    async def balance(self, ctx, *, member: discord.Member = None):
        if member == None:
            await self.open_account(ctx.author)
            user = ctx.author
            users = await self.get_bank_data()

            wallet_amt = users[str(user.id)]['wallet']
            bank_amt = users[str(user.id)]['bank']
            total_amt = wallet_amt + bank_amt

            em = discord.Embed(title=f"{ctx.author.name}'s Balance",color=embedColor)
            em.add_field(name='Wallet Balance',value = (wallet_amt), inline=False)
            em.add_field(name='Bank Balance',value = (bank_amt), inline=False)
            em.add_field(name='Total Balance',value = (total_amt), inline=False)
            await ctx.send(embed=em)

        else:
            await self.open_account(member)
            user = member
            users = await self.get_bank_data()

            wallet_amt = users[str(user.id)]['wallet']
            bank_amt = users[str(user.id)]['bank']
            total_amt = wallet_amt + bank_amt

            em = discord.Embed(title=f"{member.name}'s Balance",color=embedColor)
            em.add_field(name='Wallet Balance',value = (wallet_amt), inline=False)
            em.add_field(name='Bank Balance',value = (bank_amt), inline=False)
            em.add_field(name='Total Balance',value = (total_amt), inline=False)
            await ctx.send(embed=em)


    @commands.command()
    @cooldown(1, 20, BucketType.user)
    async def beg(self, ctx):
        users = await self.get_bank_data()
        user = ctx.author
        await self.open_account(user)



        answer = random.choice(['yes', 'no'])
        person = random.choice(['PewDiePie', 'Felix Kjellberg', 'MrBeast', 'Some guy with a hat', ])
        noResponse = random.choice(["I don't have any money right now", 
        "Uhhh. no",
        "just why?",
        "I'll come back later"])
        earnings = randint(0, 101)

        if answer == 'yes':
            await ctx.send(f"**{person}** has gave you {earnings} coins!")
            users[str(user.id)]['wallet'] += earnings
            with open('./data/mainbank.json', 'w') as f:
                json.dump(users, f)

        if answer == 'no':
            await ctx.send(f"**{person}**: {noResponse}")

    @commands.command()
    async def withdraw(self, ctx, *, amount=None):
        await self.open_account(ctx.author)
        if amount == None:
            responses = ['You sure you gon withdraw nothin?', 'aight, time to withdraw 0 coins then ']
            await ctx.send(responses)
            return

        bal = await self.update_bank(ctx.author)
        amount = int(amount)

        if amount > bal[1]:
            await ctx.send("Dude, you don't have that much money in your account")
            return

        if amount < 0:
            await ctx.send("You can't withdraw negative money, come on")
            return

        await self.update_bank(ctx.author, amount)
        await self.update_bank(ctx.author, -1*amount, 'bank')
        await ctx.send(f"You withdrew {amount} coins!")









        

def setup(client):
	client.add_cog(economy(client)) 