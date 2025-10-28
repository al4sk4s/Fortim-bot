from twitchio.ext import commands

from main import playAudio
from main import prefixo;

class Soundpad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sons")
    async def sons(self, ctx):
        await ctx.send(f"[{prefixo}risada | {prefixo}porta| {prefixo}uh | {prefixo}disse | {prefixo}ronaldo]")

    @commands.command(name="risada")
    async def risada(self, ctx):
        playAudio("risada")
    
    @commands.command(name="porta")
    async def porta(self, ctx):
        playAudio("porta")
    
    @commands.command(name="uh")
    async def uh(self, ctx):
        playAudio("uh")
    
    @commands.command(name="disse")
    async def disse(self, ctx):
        playAudio("oqeledisse")
    
    @commands.command(name="ronaldo")
    async def ronaldo(self, ctx):
        playAudio("ronaldo")

# Função obrigatória para carregar o cog
def prepare(bot):
    bot.add_cog(Soundpad(bot))
