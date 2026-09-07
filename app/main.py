import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import keep_alive

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
NEED_KEEP_ALIVE = os.getenv("NEED_KEEP_ALIVE", "false").lower() == "true"


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

@bot.command(name="ヌルポ")
async def nullpo(ctx):
    await ctx.send("ガッ")

if NEED_KEEP_ALIVE:
    keep_alive.keep_alive()

bot.run(TOKEN)
