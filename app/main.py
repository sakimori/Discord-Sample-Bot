import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import keep_alive

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
IS_KOYEB = os.getenv("KOYEB_INSTANCE_ID") is not None


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

@bot.command(name="ヌルポ")
async def nullpo(ctx):
    await ctx.send("ガッ")

if IS_KOYEB:
    keep_alive.keep_alive()

try:
    bot.run(TOKEN)
except Exception:
    if IS_KOYEB:
        os.system("kill 1")
    else:
        raise