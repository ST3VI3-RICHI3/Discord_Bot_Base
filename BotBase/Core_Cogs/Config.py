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

import discord, os
from discord.ext import commands
from BotBase import Vars
from BotBase.Vars import VDict

class Config(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["d.config"])
    async def DEV_CONFIGURE(self, ctx, *, module: str = "%VD *"):
        if ctx.author.id in VDict["Perms"]["Dev"]:

            rts = "" #Return String

            if module.startswith("%VD"):
                
                module = module.split(" ")[1]

                if module == "*":
                    for key in VDict.keys():
                        rts = f"{rts}\n{key} = {VDict[key]}"
                
                else:
                    if module in VDict.keys():
                        rts = f"Value of VDict key `{module}` is: ```{VDict[module]}```"

            await ctx.send(rts)

def setup(bot):
    bot.add_cog(Config(bot))