import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_connect():
  await client.change_presence(activity = discord.Game(name = "Hi!"))


@clientevent
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send('Hello!')
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
