import discord
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

class google_tts(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def tts(self, ctx, *, say):
        "Uses Google text to speach api to join channel and speak"
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        gTTS(say).save('media/' + say[0:25] + '.mp3')
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('media/' + say[0:25] + '.mp3'))
        ctx.voice_client.play(source)

    @commands.command()
    async def langtts(self, ctx, lang, *, say):
        "Uses Google text to speach api to join channel and speaks in the desired language"
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        gTTS(say, lang=lang).save('media/' + say[0:25] + '.mp3')
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('media/' + say[0:25] + '.mp3'))
        ctx.voice_client.play(source)



def setup(client):
    client.add_cog(google_tts(client))