from discord.ext import commands
from utils import text_to_owo

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):
        print(e)
        await ctx.send("Please check with !help the usage of this command or talk to your administrator.")

    @commands.command()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=60 * 1, max_uses=1)
        await ctx.send(link)

async def setup(bot):
    await bot.add_cog(Basic(bot))