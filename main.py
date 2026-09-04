import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import keep_alive

load_dotenv()

TOKEN = os.getenv("TOKEN")
IS_KOYEB = os.getenv("KOYEB_INSTANCE_ID") is not None


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

if IS_KOYEB:
    keep_alive.keep_alive()

try:
    bot.run(TOKEN)
except Exception:
    if IS_KOYEB:
        os.system("kill 1")
    else:
        raise