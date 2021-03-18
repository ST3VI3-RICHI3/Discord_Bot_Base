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

import os
import json
from BotBase import Vars

def Read(jsonfile: str):
    if os.path.isfile(jsonfile):
        with open(jsonfile, "r") as sf:
            S = json.load(sf)
            sf.close()
            return S
    else: return False

def dump(jsonfile: str, data):
    with open(jsonfile, "w") as sf:
        json.dump(data, sf, indent=4)
    sf.close()