# bot.py
import os

import discord
from dotenv import load_dotenv

# TESTING CREDENTIALS, REMOVE BEFORE PUSHING TO GITHUB
# client_id=840643401846147428;
# client_secret=iodDmFSUDXXirwgOVc15vSBKxDt8n-25;

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)