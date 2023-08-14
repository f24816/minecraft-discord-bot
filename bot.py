from mcstatus import JavaServer
import schedule
import discord
import time
import os
import subprocess

# Define constants
CHANNEL_ID = 0
MESSAGE_ID = 0
TOKEN = open("TOKEN", "r").read()
START_COMMAND = "./start.sh"
server = JavaServer.lookup("localhost", 25565)

def count_emoji():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(CHANNEL_ID) # Replace with your channel ID
        message = await channel.fetch_message(MESSAGE_ID) # Replace with your message ID
        reactions = message.reactions
        for reaction in reactions:
            if reaction.emoji == "👍":
                if reaction.count > 1:
                    try:
                        status = server.status()
                    except:
                        # START THE SERVER
                        await message.clear_reactions()
                        os.system(START_COMMAND)
                        print(f"An error occurred.")
        await client.close()

    # EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
    client.run(TOKEN)

def check_server():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        server = JavaServer.lookup("144.24.179.54", 25565)
        try:
            status = server.status()
            print("Players online:")
            print(status.players.online)
            if status.players.online == 0:
                time.sleep(20)
                status_new = server.status()
                if status_new.players.online == 0:
                    # STOP THE SERVER
                    print("Stopping server")
                    channel = client.get_channel(CHANNEL_ID) # Replace with your channel ID
                    message = await channel.fetch_message(MESSAGE_ID) # Replace with your message ID
                    await message.clear_reactions()
                    os.system("./stop.sh")
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
        channel = client.get_channel(CHANNEL_ID) # Replace with your channel ID
        message = await channel.fetch_message(MESSAGE_ID) # Replace with your message ID
        await message.clear_reactions()
        await client.close()

    # EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
    client.run(TOKEN)

count_emoji()
# check_server()
schedule.every(30).seconds.do(count_emoji)
schedule.every(5).minutes.do(check_server)
schedule.every(2).hours.do(clear_reactions)
print("running...")

while True:
    schedule.run_pending()
    time.sleep(1)
