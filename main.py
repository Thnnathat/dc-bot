from discord.ext import commands
import discord
import asyncio
import os
from setting import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def main():
    async with bot:
        for filename in os.listdir('./cogs'):
            if filename.endswith(".py") and filename != "__init__.py":
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.start(DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    print("run server...")
    asyncio.run(main())