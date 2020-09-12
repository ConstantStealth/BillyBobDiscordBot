from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check_any(commands.is_owner(), commands.has_role('Admin'))
    @commands.command(name='purge', brief='Purges [X] amount of messages from the chat')
    async def purge(self, ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)

    @commands.check_any(commands.is_owner())
    @commands.command(name='prune', brief='Purges inactive members from the Discord server')
    async def prune(self, ctx):
        prune_count = await ctx.guild.prune_members(days=30, compute_prune_count=True, roles=ctx.guild.roles or None,
                                      reason='Pruned for inactivity')
        await ctx.send(f'Pruned {prune_count} inactive members from the server.')

def setup(bot):
    bot.add_cog(Admin(bot))