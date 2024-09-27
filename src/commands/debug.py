from discord.ext import commands
from discord.ext.commands import Bot

class Debug(commands.Cog):

    def __init__(self, bot : Bot) -> None:
        self.__bot = bot
        super().__init__()

async def setup(bot : Bot):
    await bot.add_cog(Debug(bot))