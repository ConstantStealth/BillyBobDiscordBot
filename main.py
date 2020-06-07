from discord.ext import commands
import os

#Get token from token.txt
def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()
token=read_token()

#Command prefix
bot = commands.Bot(command_prefix='!')

#Load extensions
for filename in os.listdir("./extensions"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'extensions.{filename[:-3]}')

#Run bot with token passed
bot.run(token)