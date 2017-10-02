
import discord
from discord.ext import commands
import random
import re
import pafy
import youtube_dl
import time
import urllib
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='!', description='JeffBot')
client = discord.Client
client = bot

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


@bot.event
async def on_message(message):
    if re.search("pphedd", message.content, flags=0):
        tmp = await bot.send_message(message.channel, 'no u')

    if re.search("jeff", message.content, flags=0):
        tmp = await bot.send_message(message.channel, 'HAHAHAHAHA FUNNY MEME')
    if re.search("<244933944175362048>", message.content, flags=0):
        tmp = await bot.send_message(message.channel, 'AY DONT PING MY CREATOR')
    if re.search("(retard)|(gay)|(fag )|(faggot)|( ass )|(thot)|(fuck)|(FUCK)|(fucc)|(dinlo)|(homo )|(fuk)|(nigger)" , message.content, flags = 0):
        tmp = await bot.send_message(message.channel, 'NO BAD WORDS IN MY CHRISTIAN DISCORD')
    if re.search("dog", message.content, flags=0):
        tmp = await bot.send_message(message.channel, "Dogs aren't real duh")
    if re.search("!commie", message.content, flags = 0):
        with open('C:\\Users\\Daniel\\Desktop\\StacheBotPersonal-master\\StacheBotPersonal-master\\commie.png', 'rb') as f:
            tmp = await bot.send_file(message.channel, f)
    if re.search("jew" , message.content, flags = 0):
        tmp = await bot.send_message(message.channel, 'Here, hop into my oven!')

    await bot.process_commands(message)


@bot.command()
async def roll():
    a = random.randint(1, 20)
    await bot.say(a)

@bot.command()
async def ping():
    await bot.say("Pong!")

@bot.group()
async def play():
    print ("jeff")

@client.command(pass_context=True)
async def yt(ctx, url):
        url = ctx.message.content
        url = url.strip('!yt ')
        textToSearch = url
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        print ('https://www.youtube.com/results?search_query=' + query)

        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            if not vid['href'].startswith("https://googleads.g.doubleclick.net/‌​"):

                print ('https://www.youtube.com' + vid['href'])
                author = ctx.message.author
                voice_channel = author.voice_channel
                vc = await client.join_voice_channel(voice_channel)

                player = await vc.create_ytdl_player('https://www.youtube.com/results?search_query=' + query)
                player.start()
                while True:
                    if player.is_playing():
                        print("playing!")
                        await bot.process_commands
                    else:
                        for x in client.voice_clients:
                            if (x.server == ctx.message.server):
                                return await x.disconnect()
                                break
            break








@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    bot.say("Stopping!")

    return await client.say("I am not connected to any voice channel on this server!")

@bot.event
async def on_command_error(error, ctx):
    print (error)
    print (ctx)




bot.run('MzYwODc0NTkzOTk4NzMzMzE0.DKb6ng.v0pxoRIJ0gU4wRHOX9kH9vitmJo')
