import discord
import requests
import json
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
import time
import random
import sys
from random import random 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)
guild = "1126640367186493491"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('------')
    

'''@bot.command()
async def joke(ctx):
    """Says  Joke"""
    
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=twopart")
    data = response.text
    parse_json = json.loads(data)
    text = (parse_json["setup"])
    tex = (parse_json["delivery"])
    joke = (text) + (' ') + (tex)
    print(joke)
    await ctx.send(joke)'''

@bot.slash_command(name="joke")
async def Joke(ctx): 
    """Says  Joke"""
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=twopart")
    data = response.text
    parse_json = json.loads(data)
    text = (parse_json["setup"])
    tex = (parse_json["delivery"])
    joke = (text) + (' ') + (tex)
    print(joke)
    await ctx.respond(joke)

@bot.slash_command(name="pfp")
async def pfp(ctx,id):
    User = await bot.fetch_user(id)
    title="Profile Picture:" + (" ") + (id)
    #print(User.avatar)
    embed = discord.Embed(title=(title))

    embed.set_image(url=(User.avatar))

    await ctx.respond(embed=embed)
    

@bot.slash_command(name="steal")
async def steal(ctx, emoji: discord.PartialEmoji):  
    title = "Emoji:" + (" ") + (emoji.url)
    embed = discord.Embed(title=(title))

    embed.set_image(url=(emoji.url))
    await ctx.respond(embed=embed)

@bot.slash_command(name="close")
@commands.is_owner()
async def close(ctx):
    await ctx.respond("Done")
    await bot.close()

@bot.command()
async def steal(ctx, emoji: discord.PartialEmoji):
    title = "Emoji:" + (" ") + (emoji.url)
    embed = discord.Embed(title=(title))

    embed.set_image(url=(emoji.url))
    await ctx.send(embed=embed)

@bot.command()
async def pfp(ctx,id):
    User = await bot.fetch_user(id)
    title = "Profile Picture:" + (" ") + (id)
    embed = discord.Embed(title=(title))
    
    embed.set_image(url=(User.avatar))
    await ctx.send(embed=embed)

@bot.slash_command(name="embed")
async def embed(ctx, link):
    if "insta" in (link):
        insta = (link)
        insta = insta.replace("instagram", "ddinstagram")
        await ctx.respond(insta)
    if "x.com" in (link):
        twit = (link)
        twit = twit.replace("x", "fxtwitter") 
        await ctx.respond(twit)
    if "tiktok" in (link):
        tik = (link)
        tik = tik.replace("tiktok", "vxtiktok")
        await ctx.respond(tik)
@bot.command()
async def say(ctx, *, x: str):
    await ctx.send(x)

days1 = bot.create_group("monday", "tuesday", "wednesday")

days2 = bot.create_group("friday", "saturday", "sunday" )

@days1.command()
async def monday(ctx):
  await ctx.respond(f"Hello, {ctx.author}!")





bot.run(TOKEN)