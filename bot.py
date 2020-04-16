import discord
import asyncio
import random
import nekos
from discord.ext import commands, tasks
from itertools import cycle
import os
import subprocess
from textblob import TextBlob 

key = input('Input the key for yor bot')
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

#when a member joins put text
async def on_member_join(member):
    member.send('have a happy stay :), fortbuck i hate download')

#translates your phrase to damian text
@client.command()
async def dxmi(ctx, phrase):
    trans = ''
    length = len(phrase)
    for i in range (0, length):
        if phrase[i:i + 1] in 'aeiouAEIOU':
            trans = trans + 'x'
        else:
            trans = trans + phrase[i:i + 1]
    await ctx.send(trans)

#just a dos attack
@client.command()
async def ddos(ctx, ip):
    os.system('timeout 3 ping ' + ip + ' -c 5')
    await ctx.send('pinged ' + ip + ' 5 times for 3 seconds')

#spams a message the specified amount of times
@client.command()
async def spam(ctx, msg, nummy):
    for i in range(0, int(nummy)):
        await ctx.send(msg + ' ' + str(i + 1))

#adds 2 numbers
@client.command()
async def scumcalc_add(ctx, num1, num2):
    calc = float(num1) + float(num2)
    await ctx.send(calc)

#multiplies 2 numbers
@client.command()
async def scumcalc_mult(ctx, num1, num2):
    calc = float(num1)*float(num2)
    await ctx.send(calc)

#divides 2 numbers
@client.command()
async def scumcalc_div(ctx, nummy1, nummy2):
    calc = float(nummy1)/float(nummy2)
    await ctx.send('here youb go fathead :() ' + str(calc))

#neko.life api commands  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#sendds cat image
@client.command()
async def kitty(ctx):
    await ctx.send(nekos.cat())

#sends a fun fact
@client.command()
async def funfact(ctx):
    await ctx.send(nekos.fact())

#sends a very thought provoking question
@client.command()
async def sxd(ctx):
    await ctx.send(nekos.why())

#sends an anime
@client.command()
async def neko(ctx):
    await ctx.send(nekos.img('neko'))

#sends anime, the amount of times specified
@client.command()
async def nekospam(ctx, num):
    for i in range(1, int(num)):
        await ctx.send(nekos.img('neko'))

#sends hentai... however many times you need, no nsfw check as its funny spamming this command everywhere
@client.command()
async def hentaispam(ctx, num):
    for i in range(1, int(num)):
        await ctx.send(nekos.img('hentai'))

#sends hentai but also checks if its a nsfw enabled channel
@client.command()
async def hentai(ctx):
    if ctx.channel.is_nsfw()==True:
        await ctx.send(nekos.img('hentai'))
    else: 
        await ctx.send('sorry buddy but this isnt a nsfw channel')

#sends a from any of the nekos.life api's categories
@client.command()
async def img(ctx, image):
    await ctx.send(nekos.img(str(image)))

#tesxt blob api commands ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#translation cpmmand
@client.command()
async def trans(ctx, text, lang):
    await ctx.send(TextBlob(text).translate(to=lang))

#presence - user setting (may be removed as is practically uselsess)
@client.command()
async def playin(ctx, gamer):
    await client.change_presence(activity=discord.Game(gamer))

#shell executes shell commands in the computer hosting the bot! - prevents usage of rm comand becase i dont want to deal with my files being deleted
@client.command()
async def shell(ctx, command):
    print (command[0:2])
    if command[0:2] == 'rm':
        await ctx.send('nanana fathead your not deleting anyyything from this computer')
    else:
        og_output = subprocess.check_output(str(command),shell=True)
        formatted_output = str(og_output).replace('\\n', '\n')[2:2000]
        await ctx.send(formatted_output[:-2])

#sends invite link for the bot as i cant be bothered to make it myself anymore
@client.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=436175838363385866&scope=bot&permissions=8%27)/n/n/n@client.event/nasync')

#presence - automatic cylce
status = cycle(['github.com/sick-tichun', 'with your mum(s)', 'cashin checks', 'hittin it out da glass', 'sub2 tichun on yt', 'doin ya mom', 'clownin and keepin it rock']) #list of all clycling names
@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#the secret key!
client.run(key)