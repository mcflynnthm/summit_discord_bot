
# bot.py
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
import os

# token
TOKEN=os.getenv("DISCORD_TOKEN")

# Create bot obj

client = Bot(command_prefix="!")

# define function for on_ready
@client.event
async def on_ready():
   print("The bot is ready for vengeance.")

# define function for on_message
@client.event
async def on_message(message):
   print(message.author.name+" said, '"+message.content+"'")
   myChannel=client.get_channel(788165007161950248)
   if not message.author.id == 788165007161950248:
      if "!greeting" in message.content.lower():
         await message.channel.send("Greetings and salutations!")
      elif "!goodbye" in message.content.lower():
         await message.channel.send("See you real soon!")
      elif "bosstones" in message.content.lower():
         await message.channel.send("AAAAAH WHAT ARE THESE NOISES?")

@client.run(TOKEN)