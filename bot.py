import os
import discord
from discord.ext import commands
import re
import pyfiglet
import json

def figlateIt(msg):
    msgs = msg.split(" ")
    if msgs[0] != "~f":
        return 0
    msg = msg.replace("~f", "")
    msg = msg[1:]
    result = pyfiglet.figlet_format(msg)
    print(msg)
    print(result)
    return result


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # print(message)
        print('Message from {0.author}: {0.content}'.format(message))
        msg = message.content
        if message.content.startswith('~f'):
            figlate = figlateIt(msg)
            await message.channel.send(figlate)

client = MyClient()


if __name__ == "__main__":
    token = str(os.environ.get('bot_token'))
    client.run(token)

