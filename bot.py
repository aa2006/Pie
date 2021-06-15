import discord
import os
from discord.ext import commands

# It is my first time using Python, so there is probably bugs in this to be expected.

TOKEN = 'PASTE TOKEN HERE'

client = commands.Bot(command_prefix= 't!')

@client.event
async def on_ready():
    print('Starting up...')

## For the next 10 or so lines of code, any file ending with .py in the 'cogs' folder will be loaded (ie: translate.py)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)