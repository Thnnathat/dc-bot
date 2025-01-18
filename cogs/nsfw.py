from discord.ext import commands
import discord

from utils import get_momma_jokes

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_momma_jokes()
        if member is not None:
            await ctx.send("%s eat this: %s" % (member.name, insult))
        else:
            await ctx.send("%s %s" % (ctx.message.author.name, insult))

async def setup(bot):
    await bot.add_cog(NSFW(bot))