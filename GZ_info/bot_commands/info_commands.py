
from discord.ext import commands
from discord.channel import DMChannel

import datetime
import logging

logger = logging.getLogger('event')


class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




class Test(Cog_Extension):


    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f"!Hi <@{ctx.author.id}>")



async def setup(bot):
    await bot.add_cog(Test(bot))




