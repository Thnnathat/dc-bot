from discord.ext import commands

import random

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Give a random number between 1 and 100")
    async def roll(self, ctx):
        n = random.randrange(1, 101)
        await ctx.send(n)

    @commands.command(brief="Random number between 1 and 6")
    async def dice(self, ctx):
        n = random.randrange(1, 6)
        await ctx.send(n)

    @commands.command(brief="Either Heads or Tails")
    async def coin(self, ctx):
        n = random.randrange(0, 1)
        await ctx.send("Heads" if n == 1 else "Tails")

async def setup(bot):
    await bot.add_cog(Gamble(bot))