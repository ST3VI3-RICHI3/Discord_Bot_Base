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

from discord.ext import commands
from async_timeout import timeout
import platform
import sys
import os
from BotBase import Vars
from BotBase.Vars import VDict
from BotBase.Core.Print import prt as print

class GitControl(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if hasattr(ctx.command, "on_error"):
				return

		O = "An error has occured: \n\n--ST3VI3'S ERROR HANDLER--\n\n  "  # output
		if ctx.command != None:
			O = f"{O}Command: {ctx.command}\n  "

		#Below is temporarily disabled. The intention is to print back cog name and line number for error.
		#try:
			#error
		#except:
			# exc_type, exc_obj, exc_tb = sys.exc_info()
			# fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			#O = f"{O}File: {error.__traceback__.tb_frame.f_code.co_filename}\n  Line: {error.__traceback__.tb_lineno}\n  "

		error = getattr(error, 'original', error)

		Severity = "Undetermined"
		Class = "Unknown"
		if isinstance(error, commands.MissingRequiredArgument):
			Severity = "Unimportant"
			Class = "User invoked"
		if isinstance(error, commands.BadArgument):
			Severity = "Unimportant"
			Class = "User invoked"
		if isinstance(error, commands.CommandNotFound):
			Severity = "Unimportant"
			Class = "User invoked"
		if isinstance(error, commands.CommandInvokeError):
			Severity = "Medium"
			Class = "Code error"
		if isinstance(error, AttributeError):
			Severity = "Medium"
			Class = "Code error / Var error"
		if isinstance(error, UnboundLocalError):
			Severity = "Critical"
			Class = "Code error / Var print"

		O = f"{O}Error: {str(error)}\n  Error type: {str(type(error))[8:-2]}\n  Error class: {Class}\n  Sverity: {Severity}\n  "

		O = f"{O}\n--------------------------"
		print(O, type="err")
		await ctx.send(f"```{O}```")

def setup(bot):
    bot.add_cog(GitControl(bot))
