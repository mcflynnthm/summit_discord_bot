
# bot.py
# 2020 mcflynnthm
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
import os

## token
TOKEN=os.getenv("DISCORD_TOKEN")

## Create bot obj

client = Bot(command_prefix="!")

## define function for on_ready
@client.event
async def on_ready():
   print("The bot is ready for vengeance.")

## define function for on_message
@client.event
async def on_message(message):
   ## Print trigger message to server console
   #print(message.author.name+" said, '"+message.content+"'")
   #myChannel=client.get_channel(788165007161950248)
   myChannel=message.channel
   if not message.author.id == 788165007161950248:
      if "!greeting" in message.content.lower():
         await message.channel.send("Of greetings...")
      elif "!goodbye" in message.content.lower():
         await message.channel.send("...and goodbyes.")
         ## who doesn't like AFI amirite
      elif "bosstones" in message.content.lower():
         ## check the server for the mmb emoji
         mmb_emoji = discord.utils.get(message.guild.emojis, name = "mmb")
         # await message.channel.send("AAAAAH WHAT ARE THESE NOISES?")
         ## apply reaction if exists on server
         if mmb_emoji:
            await message.add_reaction(mmb_emoji)

client.run(TOKEN)