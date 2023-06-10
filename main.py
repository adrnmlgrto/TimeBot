import logging
import os

from bot import TimeBot
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Loading the environment variables from `.env` file.
load_dotenv()

# Getting the token from the `.env` file.
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

# Run the bot
if __name__ == "__main__":
    client = TimeBot()
    client.run(TOKEN)
