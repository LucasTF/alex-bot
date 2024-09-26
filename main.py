import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True

bot = commands.Bot(command_prefix=".", intents=permissions)

load_dotenv()

@bot.event
async def on_message(message: discord.Message):
    if message.author.id == 439614484928135188 and len(message.mentions) > 0:
        print(message.content)
        channel = message.channel
        await message.delete()
        await channel.send("kkkk censurei. 🔨👨‍🦲")


@bot.command(name="test")
async def test(ctx: commands.Context):
    await ctx.reply("O senhor tem 48 horas para se explicar.")

if __name__ == "__main__":
    bot.run(os.getenv("BOT_KEY"))