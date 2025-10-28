from twitchio.ext import commands

class Basico(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi")
    async def oi(self, ctx):
        await ctx.send(f"Olá, {ctx.author.name}! 👋")

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong! 🏓")

# Função obrigatória para carregar o cog
def prepare(bot):
    bot.add_cog(Basico(bot))