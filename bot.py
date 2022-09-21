from email import message
from utils import load_config

import discord
import random

class ChrogBot(discord.Client):
    def load_config(self):
        self.config = load_config("config.json")

    def magic_8_ball(self):
        return random.choice(self.config["8ball"])

    async def on_ready(self):
        print('Logged on as', self.user)
        self.load_config()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == "!reload":
            self.load_config()

        if message.content == "!8ball":
            await message.channel.send(self.magic_8_ball())

        if "ajay" in message.content:
            await message.channel.send('<:ajay:1021075169638350998>')
