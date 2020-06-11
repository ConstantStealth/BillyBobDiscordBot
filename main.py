from discord.ext import commands
import os
from confidential import TOKEN

# Command prefix
bot = commands.Bot(command_prefix='.')

# Load extensions
for filename in os.listdir("./extensions"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'extensions.{filename[:-3]}')

# Run bot with token.txt passed
bot.run(TOKEN)