from discord.ext import commands
import discord
import subprocess
import asyncio
from confidential import terraria_ip,terraria_port

class Terraria(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Checks the current status of the Terraria server
    @commands.command(brief='- Displays the current status of the Terraria server.')
    async def tstatus(self, ctx):
        await ctx.send('Pinging Terraria Server... ' 'This can take up to 30 seconds.')
        cmd = 'nc -vz -w 30 ' + terraria_ip +' ' + terraria_port
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        if proc.returncode == 0:
            await ctx.send('The Terraria server is currently up ' +ctx.message.author.mention)
        else:
            await ctx.send('The Terraria server is currently down ' +ctx.message.author.mention)

# Displays Terraria Server IP and Port
    @commands.command(brief='Displays Terraria Server IP and Port')
    async def tinfo(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_green())

        embed.add_field(name='Server IP', value=terraria_ip, inline=False)
        embed.add_field(name='Server Port', value=terraria_port, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Terraria(bot))