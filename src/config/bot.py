import os
import discord
from discord.ext.commands import Bot

class DiscordBot(Bot):

    def __init__(self) -> None:
        permissions = discord.Intents.default()
        permissions.message_content = True
        permissions.members = True

        self.__token = os.getenv("BOT_KEY")

        super().__init__(command_prefix=".", intents=permissions)

    async def on_ready(self):
        # for command in os.listdir(os.path.join(os.getcwd(), '/src/commands')):
        #     if (command == "__init__.py"): 
        #         continue

        #     await self.load_extension(f"commands.{command[:-3]}")

        print(os.getcwd())

    async def on_message(self, message : discord.Message):
        if message.author.id == 439614484928135188 and len(message.mentions) > 0:
            print(message.content)
            channel = message.channel
            mention = message.mentions[0]
            await message.delete()
            await channel.send(f"**Ordem Judicial**\n\nDetermino a remoção imediata de todas as mensagens enviadas por Guilherme que contenham menções ou marcas ao cidadão **{mention.display_name}** na plataforma Discord. Tal medida é necessária para preservar a ordem e a integridade do ambiente virtual, evitando a disseminação de conteúdo que possa causar dano à reputação do referido cidadão.\n\nO cumprimento desta ordem deve ser realizado sem delongas, com a devida documentação das ações tomadas.\n\nPublique-se. Cumpra-se.")
            return
        
        await self.process_commands(message)

    def run(self):
        super().run(self.__token)

discord_bot = DiscordBot()