import discord, asyncio, random, os, subprocess, json, requests, sys, shutil
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

import emojilist
from io import BytesIO
from tempfile import TemporaryFile

key = open("key.txt", "r").read()
if key == '':
    print('key file is empty, please place bot token inside key.txt')
    sys.exit()

client = commands.Bot(command_prefix = 'n')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

#when a member joins put text
@client.event
async def on_member_join(member):
    member.send('have a happy stay')

verbose = False
@client.command()
async def verbose_mode(ctx, YorN : str):
    "Verbose mode sends every message sent to the server to the users dms and logs all messages into a file.  to use verbosemode use the command with y/n after it; to check verbosemode's status, do verbose_mode ?" 
    global verbose
    if YorN == 'y':
        verbose = True
    if YorN == 'n':
        verbose = False
    if YorN == '?':
        await ctx.send("Currently verbose mode is set to : %s" % str(verbose))

funny = False
@client.command()
async def funny_mode(ctx, YorN : str):
    "Funnymode makes funnies! to use funnymode use the command with y/n after it; to check funnymode's status, do funnymode ?"
    global funny
    if YorN == 'y':
        funny = True
    if YorN == 'n':
        funny = False
    if YorN == '?':
        await ctx.send("Currently Funny mode is set to : %s" % str(funny))

#@client.command()
#async def scum(ctx):
#    await ctx.send(random.choice(ctx.guild.members))
#    print(ctx.guild.name)
#    print(ctx.author)



#loads coggsz
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename.startswith('func') == False:
        client.load_extension(f'cogs.{filename[:-3]}')

#constant runnerrsss~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@client.event # the on_message function section, most of these are toggled on/off by other varibles above
async def on_message(ctx):
    if verbose == True:
        #await ctx.send(str(ctx.author) + ' just sent: ' + ctx.content)
        logger = open(ctx.guild.name + "_log.txt", "a+")
        logger.write(str(ctx.author) + ': ' + str(ctx.content) + '\r\n')
    
    if funny == True:
        reaction_choice = random.randint(0, 100)
        if reaction_choice == 0:            
            await ctx.add_reaction('🇾')
            await ctx.add_reaction('🅾️')
            await ctx.add_reaction('🇷')
            await ctx.add_reaction('Ⓜ️')
            await ctx.add_reaction('🇺')
            await ctx.add_reaction('🇲')
            await ctx.add_reaction('🇫')
            await ctx.add_reaction('🅰️')
            await ctx.add_reaction('🇹')
        if reaction_choice == 1:
            await ctx.add_reaction('😹')
        if reaction_choice == 2:
            await ctx.add_reaction('😱')
        if reaction_choice == 3:
            await ctx.add_reaction('😐')
        if reaction_choice == 4:
            await ctx.add_reaction('👶')
        if reaction_choice == 5:
            await ctx.add_reaction('🍔')
        if reaction_choice == 6:
            await ctx.add_reaction('🇵🇰')
        if reaction_choice == 7:
            await ctx.add_reaction('🕍')
        if reaction_choice == 8:
            await ctx.add_reaction('🕋')
        if reaction_choice == 9:
            await ctx.add_reaction('😬')
        if reaction_choice == 10:
            await ctx.add_reaction('😅')
        if reaction_choice >= 11:
            randy = random.randint(0, len(emojilist.emojis))
            await ctx.add_reaction(emojilist.emojis[randy:randy+1])
    await client.process_commands(ctx)


#presence - automatic cylce
status = cycle([
'github.com/sick-tichun',
'with your mum(s)',
'cashin checks',
'hittin it out da glass',
'sub2 tichun on yt',
'doin ya mom',
'clownin and keepin it rock']) #list of all clycling names
@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(key)