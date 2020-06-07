from discord.ext import commands
import discord
import subprocess
import asyncio

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    IP = '192.168.0.0'
    PORT = '7777'

#Checks the current status of the Terraria server
    @commands.command(brief='- Displays the current status of the Terraria server.')
    async def tstatus(self, ctx):
        message = 'Pinging Terraria Server... ' 'This can take up to 30 seconds.'
        await ctx.send(message)
        cmd = ('nc -vz -w 30 ' + self.IP +' ' + self.PORT)
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        if proc.returncode == 0:
            await ctx.send('The Terraria server is currently up ' +ctx.message.author.mention)
            await ctx.delete_message(message)
        else:
            await ctx.send('The Terraria server is currently down ' +ctx.message.author.mention)
            await ctx.delete_message(message)

#Displays the Terraria server IP and Port
    @commands.command(brief='- Displays the Terraria Server IP and Port')
    async def tinfo(self, ctx):
        await ctx.send('Terraria Server IP: ' + self.IP +
                       'Server Port: ' + self.PORT)

def setup(bot):
    bot.add_cog(Game(bot))