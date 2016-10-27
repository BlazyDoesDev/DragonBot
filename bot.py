#!/usr/bin/python
import discord
import asyncio
import os
from discord.ext import commands
from cleverbot import Cleverbot as Clv
    
# from cleverbot import cleverbot


client = discord.Client()
# cb = cleverbot()


@client.event
async def on_ready():
        print('-------------')
        print('Okay, Everything seems okay - lets fly!')
        print('Im logged in as ' + client.user.name)
        print('The bots user id is ' + client.user.id)
        print('Lets go..')
        print('My oauth link is https://discordapp.com/oauth2/authorize?&client_id=241214797478232064&scope=bot&permissions=8') # TODO - Make 
        print('-------------')
    
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!!sleep'):
                await asyncio.sleep(5)
                await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!!about'):
                await asyncio.sleep(5)
                await client.send_message(message.channel, 'Hi im DragonBot')
                await client.send_message(message.channel, 'I was devloped by @Blazy#2607')
                await client.send_message(message.channel, 'If you need help or want to report a bug, Go here')
                await client.send_message(message.channel, 'https://discord.gg/HNjY8jU')
                await client.send_message(message.channel, 'Review the code at https://github.com/BlazyDoesDev/DragonBot/tree/indev')
                await client.send_message(message.channel, '***Note*** This bot is in indev, Their will be a massive ammount of bugs, plz dont hate me :(')
                


client.run('MjQxMjE0Nzk3NDc4MjMyMDY0.CvO1_Q.X3ODeYDMUWJpw54oojwe-eM-PGI') # This is a invailad token lol
