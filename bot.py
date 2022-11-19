# bot.py
import os
import random

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

bot.run(TOKEN)
