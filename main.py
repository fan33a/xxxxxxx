import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@clientevent
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startwith('hi'):
        await message.channel.send('Hello!'):
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
