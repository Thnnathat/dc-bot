from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *args):
        await ctx.send(", ".join(args))

async def setup(bot):
    await bot.add_cog(Test(bot))