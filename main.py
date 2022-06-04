import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('Fan3a')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "ملل😴", url = "https://www.twitch.tv/Fan3a"))


client.run(Fan3a)
