import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import web_server

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
LOCAL_MODE = os.getenv("LOCAL_MODE", "false").lower() == "true"

if TOKEN is None:
    raise RuntimeError("Bot Token is not set")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

@bot.command(name="ヌルポ")
async def nullpo(ctx):
    await ctx.send("ガッ")

if not LOCAL_MODE:
    web_server.keep_alive()

bot.run(TOKEN)
