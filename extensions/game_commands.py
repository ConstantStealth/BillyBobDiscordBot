from discord.ext import commands
import discord
import subprocess
import asyncio

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='- Displays the current status of the Terraria server.')
    async def tstatus(self, ctx):
        await ctx.send('Pinging Terraria Server... ' 'This can take up to 30 seconds.')
        cmd = 'nc -vz -w 30 theboisterraria.ddns.net 7777'
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        if proc.returncode == 0:
            await ctx.send('The Terraria server is currently up ' +ctx.message.author.mention)
        else:
            await ctx.send('The Terraria server is currently down ' +ctx.message.author.mention)

def setup(bot):
    bot.add_cog(Game(bot))