import discord
import json

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as test')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('hello!')

client.run(data['TOKEN'])


