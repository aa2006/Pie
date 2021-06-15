from aioify import aioify
import discord
from discord.ext import commands


from googletrans import Translator
translator = Translator()

class Translate(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.translate = aioify(Translator, name='translator')

    @commands.Cog.listener()
    async def on_ready(self):
        print("Translate module is loaded!") ## Loads module

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def translate(self, ctx, language, *, message):
        await ctx.send("Translate")

def setup(client):
    client.add_cog(Translate(client))