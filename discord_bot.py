from discord.ext import commands
from dotenv import load_dotenv

import discord
import os
import random

intents = discord.Intents.default()  
load_dotenv()
TOKEN = os.getenv('TOKEN')
intents.message_content = True
client = discord.Client(intents = intents, command_prefix="!*")

@client.command()
async def ping(ctx):
  await ctx.send('Pong!')


@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel)
    print(username, user_message, channel)

client.run(TOKEN)