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

import discord
from discord.ext import commands
from async_timeout import timeout
import platform
import os
from BotBase import Vars
from BotBase.Vars import VDict
from BotBase.Core.Print import prt as print

class RemoteControl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["d.shutdown"])
    async def DEV_SHUTDOWN(self, ctx):
        if ctx.author.id in VDict["Perms"]["Dev"]:
            print("Bot shutting down.")
            for cog in Vars.Loaded_Cogs:
                self.bot.unload_extension(cog)
            exit()

    @commands.command(aliases=["d.restart"])
    async def DEV_RESTART(self, ctx):
        if ctx.author.id in VDict["Perms"]["Dev"]:
            print("Bot restarting.")
            for cog in Vars.Loaded_Cogs:
                self.bot.unload_extension(cog)
            if platform.system().lower() == "windows":
                os.system("start bot.py")
            else:
                os.system("python bot.py")
            exit()
    
    @commands.command(aliases=["d.Rcon", "d.RCon", "d.rcon"])
    async def DEV_REMOTE_CONSOLE(self, ctx, *, cmd: str):
        if ctx.author.id in VDict["Perms"]["Dev"]:
            CmdO = os.popen(cmd).read()
            if CmdO != "": await ctx.send(f"Command returned: ```{str(CmdO)}```")
            else: await ctx.send("Command returned no output.")
            print(f"Rcon command (\"{cmd}\") returned: {str(CmdO)}")

def setup(bot):
    bot.add_cog(RemoteControl(bot))
