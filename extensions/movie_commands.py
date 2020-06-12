from datetime import datetime
import json
import pprint
import sqlite3

import aiohttp
import asyncio
import logging

import discord
from discord.ext import commands

from confidential import omdb_key

class Movie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info')
    async def info(self, ctx, *, movie):
        """Lookup a T.V. show or movie."""
        print(f'Checking for {movie}.')
        link = f'http://www.omdbapi.com/?apikey={omdb_key}&t={movie}'
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                data = await resp.json()

                success = data['Response']
                if success == 'False':
                    omdb_error = data['Error']
                    await ctx.send(f'{omdb_error}')
                elif success == 'True':
                    genre = data['Genre']
                    released = data['Released']
                    plot = data['Plot']
                    runtime = data['Runtime']
                    imdbID = data['imdbID']
                    imdbLink = f'https://www.imdb.com/title/{imdbID}/'
                    director = data['Director']

                    movie_title = data['Title']
                    year = data['Year']
                    title = f'{movie_title} ({year})'
                    embed = discord.Embed(title=title,
                                            description=plot,
                                            color=0xf5d142,
                                            url=imdbLink)

                    details = f'{runtime} | {genre} | {released}'
                    embed.add_field(name='Starring',
                                    value=data['Actors'],
                                    inline=False)
                    embed.add_field(name='Details',
                                    value=details)
                    embed.add_field(name='Director',
                                    value=f'Directed by {director}',
                                    inline=False)
                    embed.set_image(url=data['Poster'])
                    await ctx.channel.send(embed=embed)
                else:
                    print('Unexpected status.')

def setup(bot):
    bot.add_cog(Movie(bot))