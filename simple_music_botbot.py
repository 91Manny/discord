import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = Bot(command_prefix=('!', '?'))
TOKEN = 'NTgxOTUwODA5Mzc4NTIxMTI4.XQAOuA.wPq1RhoqaQvqqf3gBUlApKNoDMI'

def get_proper_channel(channel_name):
    for channel in bot.get_all_channels():
        if channel.name == channel_name and channel.type is discord.ChannelType.voice:
            return channel


@bot.command(name='play',
            description="Starts playing a YouTube song",
            brief="Play music",
            aliases=['start', 'music', 'playmusic', 'jam', 'rockout'],
            pass_context=True)
async def play(context):
    voice_channel = get_proper_channel('General')
    voice = await bot.join_voice_channel(voice_channel)
    player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=SXtYbaHP2As')
    player.start()


bot.run(TOKEN)