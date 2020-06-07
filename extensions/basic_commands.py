from discord.ext import commands
import discord

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='- Pings BillyBobDiscordBot')
    async def ping(self, ctx):
            await ctx.send('Pong!')

def setup(bot):
    bot.add_cog(Basic(bot))