
import discord
from discord.ext import commands
import random
import re
bot = commands.Bot(command_prefix='.', description='JeffBot')
client = discord.Client

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
    if re.search("<@!244933944175362048>", message.content, flags=0):
        tmp = await bot.send_message(message.channel, 'AY DONT PING MY CREATOR')
    if re.search("retard|gay|fag|faggot|ass|thot|fuck|FUCK|fucc|succ|dinlo|homo|fuk|nigger" , message.content, flags = 0):
        tmp = await bot.send_message(message.channel, 'NO BAD WORDS IN MY CHRISTIAN DISCORD')
    if re.search("dog", message.content, flags=0):
        tmp = await bot.send_message(message.channel, "Dogs aren't real duh")
    if re.search(".commie", message.content, flags = 0):
        with open('Desktop/spaghettibot/commie.png', 'rb') as f:
            tmp = await bot.send_file(message.channel, f)

    await bot.process_commands(message)


@bot.command()
async def roll(self):
    a = random.randint(1, 20)
    await bot.say(a)

@bot.command()
async def ping(self):
    await bot.say("Pong!")






@bot.event
async def on_command_error(error, ctx):
    print (error)
    print (ctx)




bot.run('MzYwODc0NTkzOTk4NzMzMzE0.DKb6ng.v0pxoRIJ0gU4wRHOX9kH9vitmJo')
