import requests
from twitchio.ext import commands

from main import prefixo;
from main import webhook;

class AudioRequest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="request")
    async def request(self, ctx, som = None):
        if som == None:
            await ctx.send(f"Você usa assim -> [{prefixo}request ronaldo] para sugerir um audio!")
        else:
            data = {
                "content": f"{ctx.author.name} Sugeriu: {som}",
                "username": ctx.author.name
            }

            try:
                response = requests.post(webhook, json=data)
                response.raise_for_status()
                await ctx.send("Request enviado!")
            except requests.exceptions.RequestException as e:
                #print(f"Error sending webhook: {e}")
                await ctx.send("Não consegui executar o comando... reclama com o dono")
    
    @commands.command(name="sugestao")
    async def sugestao(self, ctx, sugestao = None):
        if sugestao == None:
            await ctx.send(f"Você usa assim -> [{prefixo}sugestao (uma sugestão ou feedback)] para enviar uma sugestão ao meu discord!")
        else:
            data = {
                "content": f"{ctx.author.name} Sugeriu: {sugestao}",
                "username": ctx.author.name
            }

            try:
                response = requests.post(webhook, json=data)
                response.raise_for_status()
                await ctx.send("Sugestão enviada! Agradeço pelo feedback")
            except requests.exceptions.RequestException as e:
                #print(f"Error sending webhook: {e}")
                await ctx.send("Não consegui executar o comando... reclama com o dono")

def prepare(bot):
    bot.add_cog(AudioRequest(bot))
