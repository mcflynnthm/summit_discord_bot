# bot.py
# 2020 mcflynnthm

## import Discord.py elements
import discord
from discord.ext import commands

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
client = commands.Bot(command_prefix='!')

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
   myChannel=message.channel
   if not message.author.id == 788165007161950248:
      temp_time = datetime.now()
      diff = temp_time - lastrun_time
      if "bosstones" in message.content.lower():
         if diff.seconds > 300:
            ## update lastrun_time to new run time
            lastrun_time = temp_time
            await message.channel.send("AAAAAH WHAT ARE THESE NOISES?")
         ## check the server for the mmb emoji
         mmb_emoji = discord.utils.get(message.guild.emojis, name = "mmb")
         ## apply reaction if exists on server
         if mmb_emoji:
            await message.add_reaction(mmb_emoji)
   await client.process_commands(message)

@client.command(name='mute')
async def mute(ctx):
   await ctx.send("The Bot is quiet now.")

@client.command(name='muteuntil', help="HELP: tell the bot how many minutes you want it to stop yammering for.")
async def muteuntil(ctx, arg):
   if not arg:
      pass
   elif arg.len() == 0:
      pass
   else:
      await ctx.send("The Bot will be quiet until "+arg)

@client.command(name='wake')
async def wake(ctx):
   await ctx.send("The Bot has awoken. Despair.")

@client.command(name='greeting')
async def greeting(ctx):
   await ctx.send("Of greetings...")

@client.command(name='goodbye')
async def goodbye(ctx):
   await ctx.send("...and goodbyes.")

## let's start the machine
client.run(TOKEN)