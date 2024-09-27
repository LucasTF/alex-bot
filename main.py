from src.config.bot import discord_bot

# @bot.command(name="testcon")
# async def test(ctx: commands.Context):
#     await ctx.reply(f"**Ordem Judicial**\n\nDetermino a remoção imediata de todas as mensagens enviadas por Guilherme que contenham menções ou marcas ao cidadão <NOME> na plataforma Discord. Tal medida é necessária para preservar a ordem e a integridade do ambiente virtual, evitando a disseminação de conteúdo que possa causar dano à reputação do referido cidadão.\n\nO cumprimento desta ordem deve ser realizado sem delongas, com a devida documentação das ações tomadas.\n\nPublique-se. Cumpra-se.")

# @bot.event
# async def on_message(message: discord.Message):
#     if message.author.id == 439614484928135188 and len(message.mentions) > 0:
#         print(message.content)
#         channel = message.channel
#         mention = message.mentions[0]
#         await message.delete()
#         await channel.send(f"**Ordem Judicial**\n\nDetermino a remoção imediata de todas as mensagens enviadas por Guilherme que contenham menções ou marcas ao cidadão **{mention.display_name}** na plataforma Discord. Tal medida é necessária para preservar a ordem e a integridade do ambiente virtual, evitando a disseminação de conteúdo que possa causar dano à reputação do referido cidadão.\n\nO cumprimento desta ordem deve ser realizado sem delongas, com a devida documentação das ações tomadas.\n\nPublique-se. Cumpra-se.")
#         return

#     await bot.process_commands(message)

if __name__ == "__main__":
    discord_bot.run()