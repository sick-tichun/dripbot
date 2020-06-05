import discord, asyncio, random, nekos, os, youtube_dl
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import subprocess
from textblob import TextBlob, Word
import scentence_creator
import word_lsit_reader_writer
import nltk
nltk.download('wordnet')


key = open("key.txt", "r").read()
client = commands.Bot(command_prefix = '£')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

#when a member joins put text
async def on_member_join(member):
    member.send('have a happy stay')

@client.command()
async def dxmi(ctx, phrase):
    "Translates your text into: thxs (remember to put speach marks around text if your writing a scentance)"
    trans = ''
    length = len(phrase)
    for i in range (0, length):
        if phrase[i:i + 1] in 'aeiouAEIOU':
            trans = trans + 'x'
        else:
            trans = trans + phrase[i:i + 1]
    await ctx.send(trans)

@client.command()
async def ddos(ctx, ip):
    "pings an ip a couple times"
    os.system('timeout 3 ping ' + ip + ' -c 5')
    await ctx.send('pinged ' + ip + ' 5 times for 3 seconds')

@client.command()
async def spam(ctx, msg, nummy):
    "spams a message the specified amount of times"
    for i in range(0, int(nummy)):
        await ctx.send(msg + ' ' + str(i + 1))

@client.command()
async def scumcalc_add(ctx, num1, num2):
    "adds 2 numbers"
    calc = float(num1) + float(num2)
    await ctx.send(calc)


@client.command()
async def scumcalc_mult(ctx, num1, num2):
    "multiplies 2 numbers"
    calc = float(num1)*float(num2)
    await ctx.send(calc)

@client.command()
async def scumcalc_div(ctx, nummy1, nummy2):
    "divides 2 numbers"
    calc = float(nummy1)/float(nummy2)
    await ctx.send('here youb go fathead :() ' + str(calc))

@client.command()
async def invite(ctx):
    "invite link to the bot"
    await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=436175838363385866&scope=bot&permissions=8%27)/n/n/n@client.event/nasync')


#neko.life api commands  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@client.command()
async def kitty(ctx):
    "sendds cat image"
    await ctx.send(nekos.cat())

@client.command()
async def funfact(ctx):
    "sends a fun fact"
    await ctx.send(nekos.fact())

@client.command()
async def sxd(ctx):
    "sends a very thought provoking question"
    await ctx.send(nekos.why())

@client.command()
async def hentaispam(ctx, num):
    "sends hentai... however many times you want, no nsfw check :()"
    for i in range(1, int(num)):
        await ctx.send(nekos.img('hentai') + ' ' + i)

@client.command()
async def hentai(ctx):
    "sends hentai but also checks if its a nsfw enabled channel"
    if ctx.channel.is_nsfw()==True:
        await ctx.send(nekos.img('hentai'))
    else: 
        await ctx.send('sorry buddy but this isnt a nsfw channel')

@client.command()
async def img(ctx, image):
    "sends an image from any of the nekos.life api's categories"
    await ctx.send(nekos.img(str(image)))


#tesxt blob api commands ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@client.command()
async def trans(ctx, text, lang):
    "translates your message (remember speach marks!!)"
    await ctx.send(TextBlob(text).translate(to=lang))

@client.command()
async def meaning(ctx, defword):
    "defines a word"
    defenition_w = Word(defword).definitions
    await ctx.send(defenition_w)

@client.command()
async def sentence(ctx):
    "creates a (usually) gramatically scentance"
    await ctx.send(scentence_creator.create())

@client.command()
async def addword(ctx, word_to_add):
    "adds words to the scentance creation dictionary"
    word_lsit_reader_writer.word_add(word_to_add)
    await ctx.send('added ' + word_to_add + ' to the list of words')

@client.command()
async def readwords(ctx):
    "sends the entire dictionary of words so fat but gets cut off"
    await ctx.send(word_lsit_reader_writer.word_read())

@client.command()
async def shell(ctx, command):
    "shell executes shell commands in the computer hosting the bot!"
    print (command[0:2])
    if command[0:2] == 'rm':
        await ctx.send('nanana fathead your not deleting anyyything from this computer')
    else:
        og_output = subprocess.check_output(str(command),shell=True)
        formatted_output = str(og_output).replace('\\n', '\n')[2:2000]
        await ctx.send(formatted_output[:-2])



#Music Commands ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@client.command() # basically reduntant/useless
async def join(ctx):
    "Joins a voice channel"
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command("stop")
async def dc(ctx):
    "dcs from da voice"
    await ctx.voice_client.disconnect()

ffmpeg_options = {
    'options': '-vn'
}

@client.command()
async def play_local(ctx, query):
        "Plays a locally stored song"
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source)
        await ctx.send('attempting to play: {}'.format(query))


youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@client.command()
async def play(ctx, url):
    "plays vid from yt!"
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    "plays vid from yt!"

    async with ctx.typing():
        player = await YTDLSource.from_url(url, stream=True)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('Now playing: {}'.format(player.title))


#Misc ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#presence - automatic cylce
status = cycle(['github.com/sick-tichun', 'with your mum(s)', 'cashin checks', 'hittin it out da glass', 'sub2 tichun on yt', 'doin ya mom', 'clownin and keepin it rock']) #list of all clycling names
@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(key)