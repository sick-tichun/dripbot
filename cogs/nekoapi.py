import discord, nekos
from discord.ext import commands

class nekoapi(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def piss(self, ctx):
        await ctx.send('kys faggot')
        
    @commands.command()
    async def kitty(self, ctx):
        "sendds cat image"
        await ctx.send(nekos.cat())
    
    @commands.command()
    async def funfact(self, ctx):
        "sends a fun fact"
        await ctx.send(nekos.fact())
    
    @commands.command()
    async def sxd(self, ctx):
        "sends a very thought provoking question"
        await ctx.send(nekos.why())
    
    @commands.command()
    async def img(self, ctx, img):
        "sends an image from any of the nekos.life api's categories but also checks if its a nsfw enabled channel"
        if ctx.channel.is_nsfw()==True:
            await ctx.send(nekos.img(img))
        else: 
            await ctx.send('sorry buddy but this isnt a nsfw channel')
    
    @commands.command()
    async def spamimg(self, ctx, img, nummy):
        "spams a message the specified amount of times"
        for i in range(0, int(nummy)):
            await ctx.send(nekos.img(img) + ' ' + str(i + 1) + '/' + str(nummy))
    
    @commands.command()
    async def dmimg(self, ctx, user: discord.User, img, num):
        "dms nekos.life img to the specified user however many times you want"
        if int(num) > 50:
            await ctx.send('>50 too high broski')
        else:
            for i in range(0, int(num)):
                await user.send(nekos.img(img) + ' ' + str(i + 1) + '/' + str(num))


def setup(client):
    client.add_cog(nekoapi(client))
    