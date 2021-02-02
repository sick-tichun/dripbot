import discord, os, json, requests
from discord.ext import commands


class misc(commands.Cog):
    def __init__(self, client):
        self.client = client 


    @commands.command()
    async def ddos(self, ctx, ip):
        "pings an ip a couple times"
        os.system('timeout 3 ping ' + ip + ' -c 5')
        await ctx.send('pinged ' + ip + ' 5 times for 3 seconds')

    @commands.command()
    async def spam(self, ctx, msg, nummy):
        "spams a message the specified amount of times"
        if int(nummy) > 50:
            await ctx.send('>50 too high broski')
        else:
            for i in range(0, int(nummy)):
                await ctx.send(msg + ' ' + str(i + 1) + '/' + str(nummy))

    @commands.command()
    async def scumcalc_add(self, ctx, num1, num2):
        "adds 2 numbers"
        calc = float(num1) + float(num2)
        await ctx.send(calc)



    @commands.command()
    async def scumcalc_mult(self, ctx, num1, num2):
        "multiplies 2 numbers"
        calc = float(num1)*float(num2)
        await ctx.send(calc)

    @commands.command()
    async def scumcalc_div(self, ctx, nummy1, nummy2):
        "divides 2 numbers"
        calc = float(nummy1)/float(nummy2)
        await ctx.send('here youb go fathead :() ' + str(calc))

    @commands.command()
    async def invite(self, ctx):
        "invite link to the bot"
        await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=436175838363385866&scope=bot&permissions=8%27)/n/n/n@client.event/nasync')


    @commands.command()
    async def memegrab(self, ctx, memeid:str, text1:str, text2:str):
        "https://imgflip.com/popular_meme_ids"
        memejson = json.loads(requests.post(url='https://api.imgflip.com/caption_image', data = {
            'username':'chungusfan101',
            'password':'chungusfan101',
            'template_id': memeid,
            'text0': text1,
            'text1': text2,
            #'':'',
            #'':'',
            #'':'',
        }).text)
        await ctx.send(memejson['data']['url'])


    @commands.command()
    async def dm(self, ctx, user: discord.User, msg : str, num):
        "dms chosen message to specified user however many times you want"
        if int(num) > 50:
            await ctx.send('>50 too high broski')
        else:
            for i in range(0, int(num)):
                await user.send(msg + ' ' + str(i + 1) + '/' + str(num))



def setup(client):
    client.add_cog(misc(client))