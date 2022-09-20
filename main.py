import discord
import json

def load_config():
    with open("config.json") as rf:
        config = json.load(rf)
    return config

class ChrogBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        
        if "ajay" in message.content:
            await message.channel.send('<:ajay:1021075169638350998>')


config = load_config()

intents = discord.Intents.default()
intents.messages = True
bot = ChrogBot(intents=intents)
bot.run(config["token"])
