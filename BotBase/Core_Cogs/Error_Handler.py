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
from BotBase.Core.Print import prt as print
from BotBase.Vars import VDict

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, "on_error"):
            return
        
        error = getattr(error, 'original', error)

        os = f"A command caused an error:\n\n  --BOT BASE ERROR HANDLER--  \n\n    Error: {str(type(error))[8:-2]}\n           {str(error)}\n    Source: {ctx.command}\n\n  --------------------------  "
        print(os, type="err", end="\n\n")
        if ctx.author.id in VDict["Perms"]["Dev"]: await ctx.send(f"```{os}```")

def setup(bot):
    bot.add_cog(ErrorHandler(bot))