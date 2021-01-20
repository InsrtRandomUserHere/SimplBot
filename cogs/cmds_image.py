import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

embedColor = discord.Colour.from_rgb(107, 37, 249)

class ImageCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def wendys(self, ctx, *, thought):
        x = thought
        x = x.split()
        if len(x) <= 36:
            for i in range(len(x)):
                if i % 4 == 0 and i != 0:
                    x.insert(i, '\n')

            e = ' '.join(map(str, x))
            img = Image.open("MemeTemplates/wendys.jpg", 'r')
            font = ImageFont.truetype("arial.ttf", 50)
            draw = ImageDraw.Draw(img)

            draw.text((520, 110), e, (0, 0, 0), font=font, align='center')
            img.save("MemeOutputs/sir_this_is_a_wendys.jpg")
            await ctx.send(file=discord.File("MemeOutputs/sir_this_is_a_wendys.jpg"))

        elif len(x) >= 36:
            await ctx.send("Woah, that's too much. Go under the 36 character limit")

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def logic(self, ctx, *, notalogic):
        x = notalogic
        x = x.split()
        if len(x) <= 36:
            for i in range(len(x)):
                if i % 5 == 0 and i != 0:
                    x.insert(i, '\n')

            e = ' '.join(map(str, x))
            img = Image.open("MemeTemplates/logic.png").convert("RGB")

            font = ImageFont.truetype("arial.ttf", 50)
            draw = ImageDraw.Draw(img)

            draw.text((5, 10), e, (0, 0, 0), font=font, align='left')
            img.save("MemeOutputs/what_is_the_logic.png")
            await ctx.send(file=discord.File("MemeOutputs/what_is_the_logic.png"))

        elif len(x) >= 36:
            await ctx.send("Woah, that's too much. Go under the 36 character limit")

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def burn(self, ctx, *, thought):
        x = thought
        x = x.split()
        if len(x) <= 36:
            for i in range(len(x)):
                if i % 3 == 0 and i != 0:
                    x.insert(i, '\n')
            e = ' '.join(map(str, x))
            img = Image.open("MemeTemplates/burn.jpg", "r")
            font = ImageFont.truetype("arial.ttf", 25)
            draw = ImageDraw.Draw(img)

            draw.text((70, 100), e, (0, 0, 0), font=font, align='left')
            img.save("MemeOutputs/lets_burn_this.png")
            await ctx.send(file=discord.File("MemeOutputs/lets_burn_this.png"))

        elif len(x) >= 36:
            await ctx.send("Woah, that's too much. Go under the 36 character limit")

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def worthless(self, ctx, *, thing):
        x = thing
        x = x.split()
        if len(x) <= 36:
            for i in range(len(x)):
                if i % 4 == 0 and i != 0:
                    x.insert(i, '\n')

            e = ' '.join(map(str, x))
            img = Image.open("MemeTemplates/worthless.jpg", 'r')
            font = ImageFont.truetype("arial.ttf", 25)
            draw = ImageDraw.Draw(img)

            draw.text((61, 74), e, (0, 0, 0), font=font, align='center')
            img.save("MemeOutputs/woah_this_is_worthless.png")
            await ctx.send(file=discord.File("MemeOutputs/woah_this_is_worthless.png"))

        elif len(x) >= 36:
            await ctx.send("Your sentence is longer than 36 characters. Go under that limit!")

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def sleep(self, ctx, *, thing):
        x = thing
        x = x.split()
        if len(x) <= 36:
            for i in range(len(x)):
                if i % 4 == 0 and i != 0:
                    x.insert(i, '\n')

            e = ' '.join(map(str, x))
            img = Image.open("MemeTemplates/sleep.jpg", "r")
            font = ImageFont.truetype("arial.ttf", 25)
            draw = ImageDraw.Draw(img)

            draw.text((27, 338), e, (0, 0, 0), font=font, align='center')
            img.save("MemeOutputs/are_you_going_to_sleep.png")
            await ctx.send(file=discord.File("MemeOutputs/are_you_going_to_sleep.png"))

        elif len(x) >= 36:
            await ctx.send("Your sentence is longer than 50 characters. Go under that limit!")

    @commands.command(aliases=["lisa"])
    @commands.cooldown(1, 5, BucketType.user)
    async def petition(self, ctx, *, petition):
        x = petition
        x = x.split()
        if int(len(x)) <= 100:
            for i in range(len(x)):
                if i % 6 == 0 and i != 0:
                    x.insert(i, '\n')

            e = ' '.join(map(str, x))
            img = Image.open("MemeTemplates/petition.png", "r")
            font = ImageFont.truetype("arial.ttf", 40)
            draw = ImageDraw.Draw(img)

            draw.text((145, 80), e, (0, 0, 0), font=font, align='center')
            img.save("MemeOutputs/lisa_petition.png")
            await ctx.send(file=discord.File("MemeOutputs/lisa_petition.png"))

        elif int(len(x)) >= 50:
            await ctx.send("Your sentence is longer than 50 characters. Go under that limit!")

    @commands.command(case_insensitive=True)
    async def ID(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        ID = Image.open("OtherImages/Template/DiscordUserIDTemplate.png")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((264, 264))
        font = ImageFont.truetype("arlrdbd.ttf", 40)
        draw = ImageDraw.Draw(ID)

        draw.text((313, 135), user.name, (255, 255, 255), font=font, align='left')
        draw.text((313, 240), user.discriminator, (255, 255, 255), font=font, align='left')
        draw.text((313, 355), str(user.id), (255, 255, 255), font=font, align='left')
        draw.text((313, 468), str(user.created_at.date()), (255, 255, 255), font=font, align='left')
        ID.paste(pfp, (17, 102))
        ID.save("OtherImages/Output/MemberID.png")
        await ctx.send(file=discord.File("OtherImages/Output/MemberID.png"))

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def imagetest(self, ctx, *, thing):
        x = thing
        x = x.split()
        if int(len(x)) <= 2:
            for i in range(len(x)):
                if i % 4 == 0 and i != 0:
                    x.insert(i, '\n')

            e = ' '.join(map(str, x))
            img = Image.open("MemeTemplates/worthless.jpg", 'r')
            font = ImageFont.truetype("arial.ttf", 25)
            draw = ImageDraw.Draw(img)

            draw.text((61, 74), e, (0, 0, 0), font=font, align='center')
            img.save("MemeOutputs/woah_this_is_worthless.png")
            await ctx.send(file=discord.File("MemeOutputs/woah_this_is_worthless.png"))

        elif int(len(x)) >= 2:
            await ctx.send("Your sentence is longer than 36 characters. Go under that limit!")

    @commands.command()
    @commands.cooldown(1,5, BucketType.user)
    async def wanted(self, ctx, user: discord.Member):
        if user == None:
            user = ctx.author

        Template = Image.open("OtherImages/Template/DiscordUserIDTemplate.png")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((255, 255))
        draw = ImageDraw.Draw(Template)

        Template.paste(pfp, (200, 97))
        Template.save("OtherImages/Output/Wanted.png")

        await ctx.reply(file=discord.File("OtherImages/Output/Wanted.png"))







def setup(client):
    client.add_cog(ImageCmds(client))