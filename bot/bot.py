import logging

import discord
from discord import Embed

from .response import process_message

# Configure the logger
logger = logging.getLogger(__name__)

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

        except ValueError:
            await message.channel.send('U-uhm, your time format '
                                       'may be i-incorrect..')
            # Sending a GIF using a URL
            gif_url = ('https://media.tenor.com/'
                       'q3H6BzODyJAAAAAC/bocchi-bocchi-the-rock.gif')
            await message.channel.send(gif_url)
        except Exception as e:
            logging.exception(f'An error occurred when '
                              f'processing the message: {e}')
            await message.channel.send('aaAAaaAAAAAAaAAAAAAAAaAAA')
            # Sending a GIF using a URL
            gif_url = ('https://media.tenor.com/'
                       'e046riJYwWwAAAAC/bocchi-bocchi-the-rock.gif')
            await message.channel.send(gif_url)
