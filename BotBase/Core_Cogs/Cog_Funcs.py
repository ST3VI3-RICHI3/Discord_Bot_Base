"""
	Discord Bot Base, a base for discord bots
    Copyright (C) 2020  ST3VI3 RICHI3

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
from BotBase import Vars
from BotBase.Vars import VDict

class Cog_Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["d.cl"])
    async def DEV_COG_LOAD(self, ctx, cog):
        if ctx.author.id in VDict["Perms"]["Dev"]:
            try:
                self.bot.load_extension(cog)
                Vars.Loaded_Cogs.append(f"{cog}")
                await ctx.send("Cog loaded.")
            except Exception as e:
                await ctx.send(f"Failed loading extention \"{cog}\". Error: `{e}`")

    @commands.command(aliases=["d.cr"])
    async def DEV_COG_RELOAD(self, ctx, cog):
        if ctx.author.id in VDict["Perms"]["Dev"]:
            if cog.startswith("BotBase.Core_Cogs"):
                await ctx.send("Warning: Reloading this cog may result in partial or full loss of control over this bot. Type \"conf\" to confirm.")
                try:
                    async with timeout(60):
                        resp = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                except:
                    resp = "NO_RESP"
                if resp.lower() != "conf":
                    await ctx.send("Aborting command.")
                    return
            try:
                self.bot.unload_extension(cog)
                Vars.Loaded_Cogs.remove(f"{cog}")
                self.bot.load_extension(cog)
                Vars.Loaded_Cogs.append(f"{cog}")
                await ctx.send("Cog reloaded.")
            except Exception as e:
                await ctx.send(f"Failed reloading extention \"{cog}\". Error: `{e}`")

    @commands.command(aliases=["d.cu"])
    async def DEV_COG_UNLOAD(self, ctx, cog):
        if ctx.author.id in VDict["Perms"]["Dev"]:
            if cog.startswith("BotBase.Core_Cogs"):
                await ctx.send("Warning: Unloading this cog may result in partial or full loss of control over this bot. Type \"conf\" to confirm.")
                try:
                    async with timeout(60):
                        resp = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                except:
                    resp = "NO_RESP"
                if resp.lower() != "conf":
                    await ctx.send("Aborting command.")
                    return
            try:
                self.bot.unload_extension(cog)
                Vars.Loaded_Cogs.remove(f"{cog}")
                await ctx.send("Cog unloaded.")
            except Exception as e:
                await ctx.send(f"Failed unloading extention \"{cog}\". Error: `{e}`")
    
    @commands.command(aliases=["d.clist"])
    async def DEV_COG_LIST(self, ctx):
        if ctx.author.id in VDict["Perms"]["Dev"]:
            CL = "\n".join(Vars.Loaded_Cogs)
            print(Vars.Loaded_Cogs)
            await ctx.send(f"Loaded cogs:```\n{CL}```")

def setup(bot):
    bot.add_cog(Cog_Utils(bot))