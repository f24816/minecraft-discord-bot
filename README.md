# Discord Bot for managing Minecraft Servers
This bot checks for react emoji on a certain discord message, if they are enough of x emoji (check script) it starts the server. It also stops the server automatically.

It has some basic configuration:
```python
CHANNEL_ID = 0 # ID of the discord channel.
MESSAGE_ID = 0 # ID of the message.
SERVER_ADDRESS = "localhost" # Adress of the minecraft server.
START_COMMAND = "./start.sh" # Bash script to start the server.
STOP_COMMAND = "./stop.sh" # Bash script to stop the server.
EMOJI = "👍" # The emoji to look for.
EMOJI_LIMIT = 1 # The number of emojis to start the server.
