from mcstatus import JavaServer
import schedule
import discord
import time
import os

# Define constants
CHANNEL_ID = 0
MESSAGE_ID = 0
SERVER_ADDRESS = "localhost"
TOKEN = open("TOKEN", "r").read()
START_COMMAND = "./start.sh"
STOP_COMMAND = "./stop.sh"
EMOJI = "👍"
EMOJI_LIMIT = 1

def count_emoji():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        server = JavaServer.lookup(SERVER_ADDRESS, 25565)
        channel = client.get_channel(CHANNEL_ID)
        message = await channel.fetch_message(MESSAGE_ID)
        reactions = message.reactions
        for reaction in reactions:
            if reaction.emoji == EMOJI:
                if reaction.count > EMOJI_LIMIT-1:
                    try:
                        status = server.status()
                    except:
                        await message.clear_reactions()
                        os.system(START_COMMAND)
                        print(f"Server starting...")
        await client.close()
    client.run(TOKEN)

def check_server():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        server = JavaServer.lookup(SERVER_ADDRESS, 25565)
        try:
            status = server.status()
            print("Players online:")
            print(status.players.online)
            if status.players.online == 0:
                time.sleep(60)
                status_new = server.status()
                if status_new.players.online == 0:
                    # STOP THE SERVER
                    print("Stopping server")
                    channel = client.get_channel(CHANNEL_ID)
                    message = await channel.fetch_message(MESSAGE_ID)
                    await message.clear_reactions()
                    os.system(STOP_COMMAND)
                    await client.close()
        except:
            pass
    client.run(TOKEN)

def clear_reactions():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(CHANNEL_ID)
        message = await channel.fetch_message(MESSAGE_ID)
        await message.clear_reactions()
        await client.close()
    client.run(TOKEN)

print("Checking...")
count_emoji()
schedule.every(30).seconds.do(count_emoji)
schedule.every(5).minutes.do(check_server)
schedule.every(2).hours.do(clear_reactions)

while True:
    schedule.run_pending()
    time.sleep(1)
