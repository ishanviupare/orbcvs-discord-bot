import discord # using discord library

# get token from hidden file
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class Client(discord.Client):

    # bot online, display confirmation
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # prints messages in server to console live time
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

# discord intent permissions
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN) # holds token