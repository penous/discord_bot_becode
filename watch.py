import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix="?")


@bot.event
async def on_ready():
    print(f"logged on as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def yolo(ctx, *, arg):
    await ctx.send(f"{ctx.author.mention} : {arg}")


@bot.event
async def on_reaction_add(reaction, user):
    print(f"{ user } used {reaction}")
    print(f"{ reaction.message.channel.category.name}")
    if str(reaction) == "👀":
        reply = f"What are you looking at!? {reaction}"
    else:
        reply = f"you used this emoji {reaction}"
    await reaction.message.channel.send(reply)


bot.run(TOKEN)
