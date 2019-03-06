import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the official "BFF or Die" Discord Server!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='$buy'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$buy':
        await client.send_message(message.channel,'If you are interested in buying the game, here is the link: https://store.steampowered.com/app/652360/BFF_or_Die/')
    if message.content == '$updates':
        await client.send_message(message.channel,'A new character has been added in the newest update!')
client.run('NTUyNjU5NjUxMzc2ODQwNzA1.D2Cv8Q.o-c2fP1bADmT5F-TKyIdpm8PYIM')