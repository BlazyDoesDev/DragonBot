#!/usr/bin/python
import discord
import asyncio

client = discord.client
@client.event
async def on_ready():
	print('-------------')
	print('Okay, Everything seems okay - lets fly!')
	print('Im logged in as' + client.user.name)
	print('The bots user id is' + client.user.id)
	print('Lets go..')
	print('-------------')
