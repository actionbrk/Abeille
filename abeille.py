import os
import pathlib
import sys
import traceback
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

if discord_token is None:
    sys.exit("DISCORD_TOKEN introuvable")

COGS_DIR = "cogs"
DESCRIPTION = "Abeille"
bot = commands.Bot(command_prefix=commands.when_mentioned, description=DESCRIPTION)
bot.remove_command("help")


if __name__ == "__main__":
    p = pathlib.Path(__file__).parent / COGS_DIR
    for extension in [f.name.replace(".py", "") for f in p.iterdir() if f.is_file()]:
        try:
            if extension != "__init__":
                bot.load_extension(COGS_DIR + "." + extension)
                print(extension, " loaded")
        except (discord.ClientException, ModuleNotFoundError):
            print(f"Failed to load extension {extension}.")
            traceback.print_exc()


bot.run(discord_token)
