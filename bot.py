# bot.py
# 2021 mcflynnthm

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

## import Spotify stuff
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
spotify_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_sec = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_redir = os.getenv("SPOTIFY_REDIRECT_URL")

import requests

## global variables
mute_end = datetime.now()
lastrun_time = datetime.now()

## import API token from .env
TOKEN=os.getenv("DISCORD_TOKEN")

## Create bot obj
client = commands.Bot(command_prefix='!')

## define function for on_ready
@client.event
async def on_ready():
   print("The bot is ready for vengeance.")

## Checks if the bot is currently in a mute state and returns True/False
def is_muted():
   global mute_end
   diff = mute_end - datetime.now()
   if diff.total_seconds() < 0:
      return False
   else:
      return True

## define function for on_message
## this should be reserved for reactions to message content. Command definitions go below
@client.event
async def on_message(message):
   global lastrun_time
   # check if the bot sent the trigger message
   if not message.author.id == 788165007161950248:
      if "bosstones" in message.content.lower():
         diff = datetime.now() - lastrun_time
         if diff.seconds > 300 and not is_muted():
            ## update lastrun_time to new run time
            lastrun_time = datetime.now()
            await message.channel.send("AAAAAH WHAT ARE THESE NOISES?")
         ## check the server for the mmb emoji
         mmb_emoji = discord.utils.get(message.guild.emojis, name = "mmb")
         ## apply reaction if exists on server
         if mmb_emoji:
            await message.add_reaction(mmb_emoji)
   await client.process_commands(message)

## Command Definitions ##
## Command: Mute
## Description: No arguments. Mutes the bot indefinitely
@client.command(name='mute', help="shuts the bot up indefinitely. Use !wake to bring it back.")
async def mute(ctx):
   global mute_end
   ## set mute_end to 12/31/2099. I'll be dead by then probably so this code won't be my problem.
   mute_end = datetime(2099,12,31)
   await ctx.send("The Bot is quiet now.")

## Command: Muteuntil
## Description: Accepts argument of minutes. Mutes the bot for X minutes
@client.command(name='muteuntil', help="HELP: tell the bot how many minutes you want it to stop yammering for.")
async def muteuntil(ctx, arg):
   global mute_end
   if not arg:
      pass
   elif arg == "":
      pass
   else:
      mute_end = datetime.now() + timedelta(minutes = int(arg))
      await ctx.send("The Bot will be quiet until "+mute_end.strftime("%-I:%M%p %m/%d/%y"))

## Command: ismuted
## Description: Check if the bot is currently muted.
@client.command(name="ismuted", help="Checks to see if the bot is currently in a muted state, and if so, for how long.")
async def ismuted(ctx):
   if is_muted():
      await ctx.send("The bot is currently muted. It will wake up at "+mute_end.strftime("%-I:%M%p %m/%d/%y"))
   else:
      await ctx.send("The bot is not muted.")

## Command: Wake
## Description: Wakes the bot up. Doesn't care if it was actually muted or not.
@client.command(name='wake', help="Wake the bot back up.")
async def wake(ctx):
   global mute_end
   mute_end = datetime.now()
   await ctx.send("The Bot has awoken. Despair.")

## Command: pickitup
## Description: Return a random ska song
@client.command(name="pickitup", help="Gimme a random ska song, hup hup")
async def pickitup(ctx):
   pass
   #TBD: Implement *waves hands* everything
   #"q=genre:ska&type=track&offset="+randint(1,2000)

## Command: dadjoke
## Description: Return a random dad joke from the icanhazdadjoke.com API
@client.command(name="dadjoke", help="Tell me a joke. A GOOD joke.")
async def dadjoke(ctx):
   URL = "https://icanhazdadjoke.com/"
   req = requests.get(URL)
   joke = req.json()
   await ctx.send(joke['joke'])

## Command: Greeting
## Why do I still have these in here?
@client.command(name='greeting')
async def greeting(ctx):
   await ctx.send("Of greetings...")

@client.command(name='goodbye')
async def goodbye(ctx):
   await ctx.send("...and goodbyes.")

## let's start the machine
client.run(TOKEN)