import discord

from .response import process_message

__all__ = ['TimeBot']

# Defining the intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True
intents.reactions = True


class TimeBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, intents=intents, **kwargs)

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        # Ignoring the messages sent by the bot itself.
        if message.author == self.user:
            return

        try:
            # Getting the server nickname, else use username.
            nickname = message.author.nick
            if nickname is None:
                nickname = message.author.name

            # Checking if the message contains time information and respond
            response_msg = process_message(nickname, message.content)

            if response_msg:
                await message.channel.send(response_msg)
        except Exception as e:
            print(f'An error occured when getting response message: {str(e)}')
