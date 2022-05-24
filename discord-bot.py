# bot.py
import discord

bot = discord.Client()

@client.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run('MZ1yGvKTjE0rY0cV8i47CjAa.uRHQPq.Xb1Mk2nEhe-4iUcrGOuegj57zMC')