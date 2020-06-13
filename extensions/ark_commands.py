from discord.ext import commands
import discord
import subprocess
import asyncio
from confidential import ark_ip,ark_port,ark_password

class Ark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Checks the current status of the Ark server
    @commands.command(brief='- Displays the current status of the Ark server.')
    async def astatus(self, ctx):
        await ctx.send('Pinging Ark Server... ' 'This can take up to 30 seconds.')
        cmd = 'nc -vz -w 30 ' + ark_ip +' ' + ark_port
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        if proc.returncode == 0:
            await ctx.send('The Ark server is currently up ' +ctx.message.author.mention)
        else:
            await ctx.send('The Ark server is currently down ' +ctx.message.author.mention)

# Displays Ark Server IP and Port
    @commands.command(brief='Displays Ark Server IP and Port')
    async def ainfo(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_green())

        embed.add_field(name='Server IP', value=ark_ip, inline=False)
        embed.add_field(name='Server Port', value=ark_port, inline=False)
        embed.add_field(name='Server Password', value=ark_password, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ark(bot))