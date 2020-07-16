from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check_any(commands.is_owner(), commands.has_role('Admin'))
    @commands.command(name='purge', brief='Purges [X] amount of messages from the chat')
    async def purge(self, ctx, amount = 0):
        await ctx.channel.purge(limit = amount + 1)

def setup(bot):
    bot.add_cog(Admin(bot))