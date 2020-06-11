from discord.ext import commands
import discord
import datetime

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='- Pings BillyBobDiscordBot')
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command(brief='- Provides Server Statistics', description='Server Status')
    async def stats(self, ctx):
        guild = ctx.guild

        embed = discord.Embed(colour=discord.Colour.dark_green())

        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)
        no_server_members = len(guild.members)

        embed.add_field(name='Server Name', value=guild.name, inline=False)

        embed.add_field(name='# Of Server Members', value=no_server_members)

        embed.add_field(name='# Of Voice Channels', value=no_voice_channels)

        embed.add_field(name='# Of Text Channels', value=no_text_channels)

        embed.set_footer(text=datetime.datetime.now())

    @commands.command(brief='- Provides Server Statistics', description='Server Status')
    async def emotes(self, ctx):
        guild = ctx.guild

        embed = discord.Embed(colour=discord.Colour.dark_green())

        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)

        embed.add_field(name='Custom Emotes', value=emoji_string or 'No Available Emotes')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Basic(bot))