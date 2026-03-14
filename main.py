import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def status(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"Bot latency: {latency}ms")


bot.run(os.environ["DISCORD_TOKEN"])
