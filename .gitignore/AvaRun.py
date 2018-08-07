#AVA

import dbl
import discord
from discord.ext import commands

import aiohttp
import asyncio
import logging

Token = "NDc1NTcxNzYyMTQzNDI4NjA4.DkpBHw.2oKdyb2D3tlevQq787H8O_w27HI"
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("AVA AT YOUR SERVIES")

                      
@client.command()    #commands
 
async def Hi():
    await client.say("Hello!")

@client.command()    
async def Hello():
    await client.say("Hi There!")



@client.event      #costom commands
async def on_message(message):
    ask = "how are you"

    channel = message.channel
    if message.content.startswith(".how are you"):
        await client.send_message(channel, "couldn't be better \n" + ask )
    await client.process_commands(message)


@client.command(pass_context=True)   #delete command
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("messages deleted.")

client.run(Token)
