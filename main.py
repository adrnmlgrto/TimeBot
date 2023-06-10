import os
from bot import TimeBot
from dotenv import load_dotenv

# Loading the environment variables from `.env` file.
load_dotenv()

# Getting the token from the `.env` file.
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

# Run the bot
if __name__ == "__main__":
    client = TimeBot()
    client.run(TOKEN)
