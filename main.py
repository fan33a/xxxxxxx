import os
import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client = commands.Bot(
  command_prefix='409034645343174657',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "ملل😴", url = "https://www.twitch.tv/Fan3a"))


keep_alive.keep_alive()
client.run(os.getenv("Fan3a"), bot=False)


