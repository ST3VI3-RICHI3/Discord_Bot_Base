"""
	Discord Bot Base, a base for discord bots
    Copyright (C) 2021  ST3VI3 RICHI3

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import discord, os, BotBase, platform
from discord.ext import commands
from BotBase import Vars
from BotBase.Core import Settings, Intents
from BotBase.Core.Print import prt as print
from BotBase.Vars import VDict

if platform.system().lower() == "windows": VDict["IsWin"] = True

print("Bot initialising [phase 1/3]", end="\r")
Settings.Load()

print("Bot initialising [phase 2/3]", end="\r")
intents = Intents.SetIntents(discord.Intents.default(), VDict["Intents"])#Sets intents to match config
bot = commands.Bot(command_prefix=VDict["Prefix"], intents=intents)# This sets the prefix that the bot will use.
bot.remove_command('help') #Removes the default discord help command

print("Bot initialising [phase 3/3]", end="\r")
try: bot.load_extension(f"BotBase.Core_Cogs.Cog_Funcs"); Vars.Loaded_Cogs.append("BotBase.Core_Cogs.Cog_Funcs")
except: print("Failed to load core cog command (Cog_Funcs).", type="err")
try: bot.load_extension(f"BotBase.Core_Cogs.Remote_Control"); Vars.Loaded_Cogs.append("BotBase.Core_Cogs.Remote_Control")
except: print("Failed to load remote control command (Remote_Control).", type="err")
try: bot.load_extension(f"BotBase.Core_Cogs.ErrorHandler"); Vars.Loaded_Cogs.append("BotBase.Core_Cogs.ErrorHandler")
except: print("Failed to load remote control command (ErrorHandler).", type="err")
if os.path.isdir(".git"):
    try: bot.load_extension(f"BotBase.Core_Cogs.Git"); Vars.Loaded_Cogs.append("BotBase.Core_Cogs.Remote_Git")
    except: print("Failed to load remote control command (Git).", type="err")

print("Bot initialising [Done]     ")

if os.path.isdir("./Cogs"):
    print(f"Loading cogs [0/{len(Vars.Loaded_Cogs)}]", type="Cog", end="\r")
    for cog in os.listdir("./Cogs"):
        if cog.endswith(".py"):
            try:
                bot.load_extension(f"Cogs.{cog[:-3]}")
                Vars.Loaded_Cogs.append(f"Cogs.{cog[:-3]}")
                print(f"Loading cogs [{len(Vars.Loaded_Cogs)}/{len(os.listdir('./Cogs'))}]", type="Cog", end="\r")
            except Exception as e:
                print(f"Failed loading extention \"Cogs/{cog[:-3]}\". Error: {e}")
    print(f"Loading cogs [Done]                ", type="Cog",)
else:
    print("Cog directory not found, skipping cogs.", type="Cog",)

print("Bot readying...", end="\r")

@bot.event
async def on_ready():
    print("Bot ready.     ")

bot.run(BotBase.Vars.__TOKEN)
