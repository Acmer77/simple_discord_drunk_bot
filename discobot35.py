import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def get_rand_member(amount):
    membs = []
    mem_list = ''
    for server in client.servers:
        for member in server.members:
            membs.append(member)
    for i in range(amount):
        mem_list += str(random.choice(membs)) + ' '
    return (mem_list)

@client.event
async def on_message(message):
    if message.content.startswith('!drunk'):
        say = get_rand_member(3)
        printable = 'Drunk: ' + str(say)
        await client.send_message(message.channel, printable)

client.run('your-email-here', 'your-password-here')
