# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "Nzk5MjgxNDk0NDc2NDU1OTg3.YABS5g.2lmzECVlZv3vv6miVnUaKPQi2wI" # Discord Bot token for our user join bot

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)