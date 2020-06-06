import discord
import subprocess
import asyncio

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token=read_token()

client = discord.Client()

@client.event
async def on_message(message):
    #Server ID
    id = client.get_guild(546201103201599488)

    #Valid Bot Channels
    channels = ["bot-spam", "terraria-server-link"]

    #Mod List
    mod_list = ""

#Public Commands
    if str(message.channel) in channels:
        if message.content.find("!membercount") !=-1:
            await message.channel.send(f"""Number of Server Members: {id.member_count}""")
        elif message.content == "!terrariastatus":
            try:
                await asyncio.create_subprocess_shell(['nc', '-vz', '-w 30', 'theboisterraria.ddns.net', '7777'])
            except:
                await message.channel.send("it died")
            else:
                await message.channel.send("its up")

#Mod Only Commands
    if str(message.channel) in channels and str(message.author) in mod_list:
        if message.content.find("!modtest") !=-1:
            await message.channel.send("You are a mod")


client.run(token, bot=True, reconnect=True)