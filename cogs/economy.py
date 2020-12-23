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
            responses = random.choice(['You sure you gon withdraw nothin?', 'aight, time to withdraw 0 coins then '])
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

    @commands.command()
    async def deposit(self, ctx, *, amount=None):
        await self.open_account(ctx.author)
        if amount == None:
            responses = random.choice(['You sure you gon deposit nothin?', 'aight, time to deposit 0 coins then '])
            await ctx.send(responses)
            return

        bal = await self.update_bank(ctx.author)
        amount = int(amount)

        if amount > bal[1]:
            await ctx.send("Dude, you don't have that much money in your wallet")
            return

        if amount < 0:
            await ctx.send("You can't deposit negative money, come on")
            return

        await self.update_bank(ctx.author, -1*amount)
        await self.update_bank(ctx.author, amount, 'bank')
        await ctx.send(f"You deposited {amount} coins!")

    @commands.command(aliases=['send'])
    async def donate(self, ctx, member : discord.Member=None, *, amount=None):
        await self.open_account(ctx.author)
        await self.open_account(member)
        if amount == None:
            responses = random.choice(['You sure you gon donate nothin?', 'aight, time to send 0 coins then '])
            await ctx.send(responses)
            return

        if member == None:
            await ctx.send("Who are you gonna send the money to?")
            return

        bal = await self.update_bank(ctx.author)
        amount = int(amount)

        if amount > bal[0]:
            await ctx.send("Dude, you don't have that much money in your bank")
            return

        if amount < 0:
            await ctx.send("You can't send negative money, come on")
            return

        await self.update_bank(ctx.author, -1*amount, 'bank')
        await self.update_bank(member, amount, 'bank')
        await ctx.send(f"You gave {member.mention} {amount} coins!")

    @commands.command()
    async def slots(self, ctx, *, amount=None):
        await self.open_account(ctx.author)
        if amount == None:
            responses = random.choice(['how much money you gon put into this?'])
            await ctx.send(responses)
            return

        bal = await self.update_bank(ctx.author)
        amount = int(amount)

        if amount > bal[1]:
            await ctx.send("Dude, you don't have that much money in your wallet")
            return

        if amount < 0:
            await ctx.send("You can't deposit negative money, come on")
            return

        final = []
        for i in range(3):
            emojis = ['<:HouseOfBravery:791309903212838952>', '<:balance:791309928052686888>',
                      '<:HouseOfBrilliance:791310012030255115>', '<a:blurplehypesquad:791311003065384991>',
                      '<a:hypesquad:791311097760055326>', '<a:HypesquadEvents:791311131041464320>']
            a = random.choice(emojis)
            final.append(a)
        await ctx.send(str(final))
        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await self.update_bank(ctx.author, 2*amount)
            await ctx.send(f"You won {2*amount} coins!")
        else:
            await self.update_bank(ctx.author, -1*amount)
            await ctx.send(f"You lost {-1 * amount} coins")




        await self.update_bank(ctx.author, -1*amount)


        

def setup(client):
	client.add_cog(economy(client)) 