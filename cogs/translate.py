from aioify import aioify
import discord
from discord.ext import commands


from googletrans import Translator
import googletrans
translator = Translator()

class Translate(commands.Cog):

    german = "de"
    english = "en"
    spanish = "es"
    french = "fr"

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
    async def translate(self, ctx, lang, *, msg):
        if lang not in googletrans.LANGUAGES.keys():
            await ctx.send("Language provided is not specified")
            return
        else:
            translation = translator.translate(msg, dest=lang)
        await ctx.send(translation)



def setup(client):
    client.add_cog(Translate(client))