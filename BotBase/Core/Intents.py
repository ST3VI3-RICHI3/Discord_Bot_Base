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

def SetIntents(IntObj: discord.Intents, IntL):
    for intent in IntL:
        if intent == "guilds":
            IntObj.guilds = True
        elif intent == "members":
            IntObj.members = True
        elif intent == "bans":
            IntObj.bans = True
        elif intent == "emojis":
            IntObj.emojis = True
        elif intent == "integrations":
            IntObj.integrations = True
        elif intent == "webhooks":
            IntObj.webhooks = True
        elif intent == "invites":
            IntObj.invites = True
        elif intent == "voice_states":
            IntObj.voice_states = True
        elif intent == "presences":
            IntObj.presences = True
        elif intent == "messages":
            IntObj.messages = True
        elif intent == "guild_messages":
            IntObj.guild_messages = True
        elif intent == "dm_messages":
            IntObj.dm_messages = True
        elif intent == "reactions":
            IntObj.reactions = True
        elif intent == "guild_reactions":
            IntObj.guild_reactions = True
        elif intent == "dm_reactions":
            IntObj.dm_reactions = True
        elif intent == "typing":
            IntObj.typing = True
        elif intent == "guild_typing":
            IntObj.guild_typing = True
        elif intent == "dm_typing":
            IntObj.dm_typing = True
    return IntObj
