from discord.ext import commands
import discord


class Polls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Polls(bot))
