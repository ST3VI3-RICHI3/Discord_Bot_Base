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

from __future__ import print_function
from datetime import datetime
from BotBase.Core import Logging

def prt(msg:str, type="inf", start="", end="\n", log=True):
    Time = f"{str(datetime.now().day).zfill(2)}/{str(datetime.now().month).zfill(2)}/{str(datetime.now().year).zfill(4)}, {str(datetime.now().hour).zfill(2)}:{str(datetime.now().minute).zfill(2)}:{str(datetime.now().second).zfill(2)}"
    ostr = msg
    if type.lower() == "inf":
        ostr = f"{start}[{Time} | Info] {msg}"
    elif type.lower() == "err":
        ostr = f"{start}[{Time} | Error] {msg}"
    else:
        ostr = f"{start}[{Time} | {type}] {msg}"
    if log:
        Logging.Log()
    print(ostr, end=end)
