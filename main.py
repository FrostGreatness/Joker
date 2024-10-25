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
import re
from urllib.request import urlretrieve
from random import random 
import pyktok as pyk
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

#@bot.event
#async def on_message(message):
#    channel = bot.get_channel(1282479461039603732)
 #       #await channel.send(message.stickers)
#    if message.author == bot.user:
#       return
#   await channel.send(message.stickers)
    
@bot.command()
async def id(ctx):
    #await ctx.send(ctx.message.stickers)
    # [<StickerItem id=1270153970354225152 name
    await ctx.send(ctx.message.stickers)
    

@bot.slash_command(name="yoinkgif")
async def yoinkgif(ctx, id):
    sticker = "https://media.discordapp.net/stickers/" + (id) + ".gif?size=320&quality=lossless"
    title = "Animated Sticker: " + (id) + (" ") + (sticker)
    embed = discord.Embed(title=(title))
    embed.set_image(url=(sticker))
    await ctx.respond(embed=embed)
@bot.slash_command(name="yoink")
async def yoink(ctx, id):
    sticker = "https://media.discordapp.net/stickers/" + (id) + ".png?size=320&quality=lossless"
    title = "Sticker: " + (id) + (" ") + (sticker)
    embed = discord.Embed(title=(title))
    embed.set_image(url=(sticker))
    await ctx.respond(embed=embed)

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

@bot.slash_command(name="tiktok")
async def tiktok(ctx, link):
    txt = (link)

    x = (txt[23:100])
    filetxt = x.replace("/", "_" )
    path = ("D:/joker updat e/Joker/")
    
    s = (path) + (filetxt) + ('.mp4')
    if os.path.exists(s):
        os.remove(s)
    else:
        print("The file does not exist") 
    pyk.specify_browser('firefox') #browser specification may or may not be necessary depending on your local settings
    pyk.save_tiktok((link),
	        True,
                'tiktok_data.csv',
		'firefox')
    
    with open((s), 'rb') as f:
        video_file = discord.File(f)
        await ctx.respond("Here's your video:" , file=video_file)






bot.run(TOKEN)