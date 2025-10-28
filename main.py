import os
import json
import random
import dotenv
import asyncio
import winsound
import threading
from twitchio.ext import commands


# Carregando configurações e .env  ----------------------------
default_config = {"message_alerts":True, "chat_commands": True}

if not os.path.exists('config.json'):
    with open('config.json', 'w') as g:
        json.dump(default_config, g, indent=4)

with open('config.json', 'r') as f:
    config = json.load(f)

if not os.path.exists('.env'):
    with open('.env', 'w') as h:
        h.write('TOKEN=\nCHANNEL=\nPREFIX=!\nWEBHOOK=\n')

dotenv.load_dotenv(dotenv.find_dotenv())

token = os.getenv("TOKEN")
canal = os.getenv("CHANNEL")
prefixo = os.getenv("PREFIX")
webhook = os.getenv("WEBHOOK")

if os.getenv(token) == "":
    print("Você precisa escrever no .env o seu token TMI, acesse https://twitchtokengenerator.com/ para saber mais.")
    exit()

if os.getenv(canal) == "":
    print("Você precisa escrever no .env o seu canal.")
    exit()

def playAudio(nome):
    threading.Thread(target=lambda: winsound.PlaySound(os.getcwd() + rf"\sounds\{nome}.wav", winsound.SND_FILENAME)).start()
    return

# Main Classe do bot  ----------------------------
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=token,
            prefix=prefixo,  # prefixo de comandos (não usado, mas obrigatório)
            initial_channels=[canal]
        )

    async def event_ready(self):
        print(f"Conectado ao chat de {canal}!")

        # Auto-carregador de cogs
        for arquivo in os.listdir("comandos"):
            if arquivo.endswith(".py"):
                nome_modulo = f"comandos.{arquivo[:-3]}"
                try:
                    self.load_module(nome_modulo)
                    print(f"🔹 Carregado comando: {arquivo}")
                except Exception as e:
                    print(f"⚠️ Falha ao carregar {arquivo}: {e}")
        
        asyncio.create_task(self.auto_msg_loop())
    
    async def auto_msg_loop(self):
        while True:
            await asyncio.sleep(10 * 60)  # 10 minutos
            if canal:
                with open('mensagens.txt', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if lines:
                        await bot.connected_channels[0].send(random.choice(lines).strip()) # .strip() to remove newline characters

    async def event_message(self, message):
        if message.echo:
            return  # Ignora mensagens enviadas pelo bot
        
        print(f"{message.author.name}: {message.content}")
        
        if config["message_alerts"] == True and message.author.name != canal:
            # Toca som em uma thread para não travar o bot
            playAudio("alert")
        
        # Faz com que comandos também funcionem
        await self.handle_commands(message)
    
    async def event_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return

if __name__ == "__main__":
    bot = Bot()
    bot.run()