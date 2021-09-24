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

from abc import get_cache_token
import discord, os
from discord.errors import InvalidData
from discord.ext import commands
from BotBase import Vars
from BotBase.Vars import VDict

class Config(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.ModificatonBuffer = []

    @commands.command(aliases=["d.config"])
    async def DEV_CONFIGURE(self, ctx, RW:str, Target: str, Value=None): #Self, CTX, Read/Write, Target, Value
        if ctx.author.id in VDict["Perms"]["Dev"]:

            rts = "" #Return String

            Targ = Target.split(".")

            def GetKey(Targ, Wd=VDict, rts=rts):

                LI = 0 #List index

                for prop in Targ:
                    if LI > 0:
                        if type(Wd) == dict:
                            if prop in Wd.keys():
                                Wd = Wd[prop]
                                LI += 1
                        else:
                            rts = f"Error: Target `{Target}` is invalid, property {str(LI+1)} (`{Targ[LI]}`) expected dictionary, not {str(type(prop))}."
                            raise(InvalidData)
                    else:
                        LI += 1
                return Wd

            if RW.lower().startswith("r"):
                
                if Targ[0] == "VDict":
                    try:
                        t = GetKey(Targ)
                        if type(t) == dict:
                            rts = "\n    ".join(f"\"{str(k)}\": {str(t[k])}" for k in t.keys())
                            rts = f"{{\n    {rts}\n}}"
                            rts = f"Value of `{Targ[len(Targ)-1]}`: ```{rts}```"
                        else:
                            rts = f"Value of `{Targ[len(Targ)-1]}`: ```{str(t)}```"
                        
                    except:
                        pass
                else:
                    rts = f"Unknown data source `{Targ[0]}`."

            elif RW.lower().startswith("w"):
                if Value:
                    if Targ[0] == "VDict":
                        try:
                            GetKey(Targ)
                            self.ModificatonBuffer.append([Target, Value])
                            rts = f"Staged `{Targ[len(Targ)-1]}` to be upddated to value `{Value}`."
                        except:
                            pass
                    else:
                        rts = f"Unknown data source `{Targ[0]}`."
                else:
                    rts = f"No value provided."

            await ctx.send(rts)

def setup(bot):
    bot.add_cog(Config(bot))