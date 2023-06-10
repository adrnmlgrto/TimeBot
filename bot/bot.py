import discord
from discord import Embed

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
            status, data = process_message(nickname, message.content)

            if status:
                sender = data.get('author')
                unix_ts = data.get('unix_timestamp')
                orig_time_str = data.get('original_time_string')

                # Replace the original time string with the Unix timestamp
                formatted_message = message.content.replace(orig_time_str,
                                                            f"<t:{unix_ts}:t>")

                # Create an embed
                embed = Embed(
                    description=f'{formatted_message}',
                    color=0xeeb8c4
                )
                # Set the author field with the
                # message sender's icon and nickname
                embed.set_author(name=sender,
                                 icon_url=message.author.avatar.url)
                # Send the embed to the channel
                await message.channel.send(embed=embed)

        except Exception as e:
            print(f'An error occurred when getting response message: {str(e)}')
