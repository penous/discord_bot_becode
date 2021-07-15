import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="?")


@bot.event
async def on_ready():
    print(f"logged on as {bot.user}")


@bot.event
async def on_user_update(before, after):
    print(f"before: {before} and after: {after}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def test(ctx, *, arg):
    await ctx.send(f"{ctx.author.mention} : {arg}")


@bot.command()
async def pew(ctx):
    with open("users.json", r) as f:
        users = json.load(f)

    await update_data(users, ctx.message.author)


@bot.event
async def on_reaction_add(reaction, user):
    print(f"{ user } used {reaction}")
    print(f"{ reaction.message.channel.category.name}")


async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["points"] = 0
        users[user.id]["level"] = 0


bot.run("ODYzNzM4NjY2Mjk5NTU1ODUw.YOrRUQ.SYasSPLxavwv9idPATCTKCCr6N0")
