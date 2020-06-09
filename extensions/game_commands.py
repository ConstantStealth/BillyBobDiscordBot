from discord.ext import commands
import discord
import subprocess
import asyncio

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def IP(self, IP):
        self.IP = 'theboisterrariaserver.ddns.net'

    def PORT(self, PORT):
        self.PORT = '7777'

#Checks the current status of the Terraria server
    @commands.command(brief='- Displays the current status of the Terraria server.')
    async def tstatus(self, ctx):
        await ctx.send('Pinging Terraria Server... ' 'This can take up to 30 seconds.')
        cmd = ('nc -vz -w 30 ' + self.IP +' ' + self.PORT)
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        if proc.returncode == 0:
            await ctx.send('The Terraria server is currently up ' +ctx.message.author.mention)
        else:
            await ctx.send('The Terraria server is currently down ' +ctx.message.author.mention)

#Displays the Terraria server IP and Port
    @commands.command(brief='- Displays the Terraria Server IP and Port')
    async def tinfo(self, ctx):
        await ctx.send(' You can connect to the Terraria server with the below information:```Server IP: ' + self.IP + '\n'
                        'Server Port: ' + self.PORT + '```')

def setup(bot):
    bot.add_cog(Game(bot))