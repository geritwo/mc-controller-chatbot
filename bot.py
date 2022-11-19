import os

import discord
from discord.ext import commands


TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name="foo", description="Sends back whatever you type in")
async def foo(ctx, arg=""):
    res = arg if arg else "bar"
    await ctx.send(res)

bot.run(TOKEN)
