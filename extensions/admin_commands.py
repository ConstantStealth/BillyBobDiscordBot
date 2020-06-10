from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="test admin command")
    @commands.check_any(commands.is_owner(), commands.has_role('Admin'))
    async def admin(self, ctx):
            await ctx.send('test')

def setup(bot):
    bot.add_cog(Admin(bot))