
# bot.py
# 2020 mcflynnthm

## import Discord.py elements
import discord
from discord.ext.commands import Bot

## import dotenv
from dotenv import load_dotenv
load_dotenv()
import os

## import datetime and init variables
from datetime import datetime
from datetime import date
from datetime import timedelta
lastrun_time = datetime.now()

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
   global lastrun_time
   ## Print trigger message to server console
   #print(message.author.name+" said, '"+message.content+"'")
   #myChannel=client.get_channel(788165007161950248)
   myChannel=message.channel
   if not message.author.id == 788165007161950248:
      temp_time = datetime.now()
      diff = temp_time - lastrun_time
      if "!greeting" in message.content.lower():
         await message.channel.send("Of greetings...")
      elif "!goodbye" in message.content.lower():
         await message.channel.send("...and goodbyes.")
         ## who doesn't like AFI amirite
      elif "bosstones" in message.content.lower():
         if diff.seconds > 300:
            ## update lastrun_time to new run time
            lastrun_time = temp_time
            await message.channel.send("AAAAAH WHAT ARE THESE NOISES?")
         ## check the server for the mmb emoji
         mmb_emoji = discord.utils.get(message.guild.emojis, name = "mmb")
         ## apply reaction if exists on server
         if mmb_emoji:
            await message.add_reaction(mmb_emoji)

## let's start the machine
client.run(TOKEN)