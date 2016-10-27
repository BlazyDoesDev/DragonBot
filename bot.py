#!/usr/bin/python
import discord
import asyncio
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

<<<<<<< HEAD
<<<<<<< HEAD
        elif message.content.startswith('!!about'):
                await client.send_message(message.channel, 'Hi im DragonBot')
                await client.send_message(message.channel, 'I was devloped by @Blazy#2607')
                await client.send_message(message.channel, 'If you need help or want to report a bug, Go here')
                await client.send_message(message.channel, 'https://discord.gg/HNjY8jU')
                await client.send_message(message.channel, 'Review the code at https://github.com/BlazyDoesDev/DragonBot/tree/indev')
                await client.send_message(message.channel, '***Note*** This bot is in indev, Their will be a massive ammount of bugs, plz dont hate me :(')
                
        elif message.content.startswith('!!help'):
             await client.send_message(user, 'Here is a list of commands \n !!about - Tells you about bot \n !!sleep Debug Command')
                                       
                
                


client.run('MjQxMjE0Nzk3NDc4MjMyMDY0.CvO3Qg.cJO_C5TVJNYc2vsplGGQy8WhxH4') # This is a invailad token lol
=======
client.run('MjQxMjE0Nzk3NDc4MjMyMDY0.CvOwXg.fNFmbRgzItqn7loRylZLdUaOfds') # This is a invailad token lol
>>>>>>> parent of 6407d98... Added git add bot.pyabout
=======
client.run('MjQxMjE0Nzk3NDc4MjMyMDY0.CvOwXg.fNFmbRgzItqn7loRylZLdUaOfds')
>>>>>>> parent of ddc333a... hehehh kek
