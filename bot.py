import discord
import asyncio
import random
import nekos
from discord.ext import commands
from itertools import cycle
import os
import subprocess

client = commands.Bot(command_prefix = '')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def spam(ctx, msg, nummy):
    for i in range(0, int(nummy)):
        await ctx.send(msg + ' ' + str(i))

@client.command()
async def scumcalc_add(ctx, num1, num2):
    calc = float(num1) + float(num2)
    await ctx.send(calc)

@client.command()
async def scumcalc_mult(ctx, num1, num2):
    calc = float(num1)*float(num2)
    await ctx.send(calc)

@client.command()
async def scumcalc_div(ctx, nummy1, nummy2):
    calc = float(nummy1)/float(nummy2)
    await ctx.send('here youb go fathead :() ' + str(calc))

#neko.life_commands
@client.command()
async def kitty(ctx):
    await ctx.send(nekos.cat())
@client.command()
async def funfact(ctx):
    await ctx.send(nekos.fact())
@client.command()
async def sxd(ctx):
    await ctx.send(nekos.why())
@client.command()
async def neko(ctx):
    await ctx.send(nekos.img('neko'))
@client.command()
async def nekospam(ctx, num):
    for i in range(1, int(num)):
        await ctx.send(nekos.img('neko'))
@client.command()
async def hentaispam(ctx, num):
    for i in range(1, int(num)):
        await ctx.send(nekos.img('hentai'))
@client.command()
async def hentai(ctx):
    await ctx.send(nekos.img('hentai'))
@client.command()
async def img(ctx, image):
    await ctx.send(nekos.img(str(image)))
#presence - new method
@client.command()
async def playin(ctx, gamer):
    await client.change_presence(activity=discord.Game(gamer))

@client.command()
async def shell(ctx, command):
    print (command[0:2])
    if command[0:2] == 'rm':
        await ctx.send('nanana fathead your not deleting anyyything from this computer')
    else:
        og_output = subprocess.check_output(str(command),shell=True)
        formatted_output = str(og_output).replace('\\n', '\n')[1:2000]
        await ctx.send(formatted_output)

@client.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=436175838363385866&scope=bot&permissions=8%27)/n/n/n@client.event/nasync')

#presence - old cylce
pubes = [''] #list of all clycling names

#the secret key!
client.run('KEY')
