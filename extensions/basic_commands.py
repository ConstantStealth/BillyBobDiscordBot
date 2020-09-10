from discord.ext import commands
import discord
import datetime

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', brief='Pings BillyBobDiscordBot')
    async def ping(self, ctx):
        latency = round(self.bot.latency, 2)
        await ctx.send(f'Pong! ({latency}ms)')

    @commands.command(name='stats', brief='Provides Server Statistics',
                      description='Server Stats')
    async def stats(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(colour=discord.Colour.dark_green())
        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)
        no_server_members = len(guild.members)

        embed.add_field(name='Server Name', value=guild.name, inline=False)
        embed.add_field(name='# Of Server Members', value=int(no_server_members))
        embed.add_field(name='# Of Voice Channels', value=int(no_voice_channels))
        embed.add_field(name='# Of Text Channels', value=int(no_text_channels))
        embed.set_footer(text=datetime.datetime.now())

        await ctx.message.channel.send(embed=embed)

    @commands.command(name='repo', brief='Provides a link to BBDB GitHub Repository',
                      aliases=['repository'])
    async def repo(self, ctx):
        await ctx.send('You can find the BBDB GitHub repository here: https://github.com/ConstantStealth/BillyBobDiscordBot/')

def setup(bot):
    bot.add_cog(Basic(bot))