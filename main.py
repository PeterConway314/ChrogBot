import discord

from bot import ChrogBot
from utils import load_config

if __name__ == "__main__":
    token_config = load_config("token.json")

    intents = discord.Intents.default()
    intents.messages = True
    bot = ChrogBot(intents=intents)
    bot.run(token_config["token"])
