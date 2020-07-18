from discord.ext import commands
import discord
import sqlite3
import subprocess
import asyncio

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        conn = sqlite3.connect('databases/roles.db')
        c = conn.cursor()
        try:
            c.execute('CREATE TABLE IF NOT EXISTS roles(name TEXT, joinable INT)')
        except sqlite3.OperationalError as error:
            print(f'Sqlite operational error: {error}')
        conn.commit()
        conn.close()

    @commands.check_any(commands.is_owner(), commands.has_role('Admin'))
    @commands.command(name='createrole', brief='Creates a self-joinable role',
                      aliases=['newrole'])
    async def createrole(self, ctx, role: str, color: discord.Colour,
                                 joinable=True):
        conn = sqlite3.connect('databases/roles.db')
        c = conn.cursor()
        name = (role,)
        search = c.execute('SELECT * FROM roles WHERE name=?', name)
        data = c.fetchall()
        if len(data) > 0:
            await ctx.send('That role already exists.')
        elif joinable is True:
            print('Running createrole')
            await ctx.guild.create_role(name=role, color=color)
            print('Role created.')
            if joinable is True:
                # Stash the role in the database.
                data = (role, joinable)
                c.execute('INSERT INTO roles VALUES (?,?)', data)
                conn.commit()
                conn.close()
            await ctx.send('Created role {}.'.format(role))
        role_cache_updated = True

    @commands.check_any(commands.is_owner(), commands.has_role('Admin'))
    @commands.command(name='deleterole', brief='Deletes a self-joinable role',
                      aliases=['removerole'])
    async def deleterole(self, ctx, *, role_name, reason=None):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is not None:
            conn = sqlite3.connect('databases/roles.db')
            c = conn.cursor()
            name = (role_name,)
            search = c.execute('SELECT * FROM roles WHERE name=?', name)
            data = c.fetchall()
            if len(data) > 0:
                deleted = c.execute('DELETE FROM roles WHERE name=?', name)
            else:
                await ctx.send('That role does not exist.')
            conn.commit()
            conn.close()
            role_cache_updated = True
            await role.delete(reason='Removed by command')
            await ctx.send(f'Deleted role {role_name}.')
        else:
            await ctx.send(f'{role_name} does not exist.')

    @commands.command(name='joinrole', brief='Join a self-joinable role',
                      aliases=['subscribe', 'join'])
    async def joinrole(self, ctx, *, role_name: str):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is not None:
            roles = ctx.author.roles
            if role in roles:
                await ctx.author.remove_roles(role)
                await ctx.send(f'You have left {role_name}.')
            else:
                await ctx.author.add_roles(role)
                await ctx.send(f'You have joined {role_name}.')
        else:
            ctx.send('The role {role_name} doesn\'t seem to exist. Use '
                     '.roleslist to confirm.')

    @commands.command(name='rolelist', brief='Displays a list of self-joinable roles',
                      aliases=['roleslist', 'listroles'])
    async def rolelist(self, ctx):
        conn = sqlite3.connect('databases/roles.db')
        c = conn.cursor()
        joinable = (True,)
        search = c.execute('SELECT * FROM roles WHERE joinable=?', joinable)
        roles = c.fetchall()
        msg = ""
        for role in roles:
            msg = f'{msg}{role[0]}\n'
        msg = f'```\n{msg}```'
        conn.close()
        await ctx.send('Below is a list of self-joinable roles: %s' % msg)

    @commands.check_any(commands.is_owner(), commands.has_role('Admin'))
    @commands.command(name='backupdb', brief='Backup all new/updated bot files from VPS to GitHub',
                      aliases=['updatedb', 'dbupdate', 'backup'])
    async def backupdb(self, ctx):
        await ctx.send('Committing and pushing updated database to GitHub... ')
        cmd = subprocess.run('git add databases/roles.db && git commit -m "Database Update" && git push',
                             shell=True)
        if cmd.returncode == 0:
            await ctx.send('The database has been updated to GitHub')
        else:
            await ctx.send('There was an error updating the database to GitHub, the database may already be up to date.')

    @commands.command()
    async def remove(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='DELETE')


def setup(bot):
    bot.add_cog(Roles(bot))