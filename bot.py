import os

import discord
from discord.ext import commands


TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='//', intents=intents, description="A simple Discord bot")


@bot.command(name="foo", description="Sends back whatever you type in")
async def foo(ctx, arg=""):
    res = arg if arg else "bar"
    await ctx.send(res)


@bot.command(name="hello", description="Sends a hello to user")
async def hello_user(ctx):
    await ctx.send(f"Hello {ctx.author}!")


@bot.command(name="server", description="Check server stats")
async def server_control(ctx, arg):
    pass

bot.run(TOKEN)
