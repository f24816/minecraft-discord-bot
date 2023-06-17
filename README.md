# Discord Bot to start Minecraft Server
This bot checks for emoji count on a certain discord message, if the number is bigger than X it starts the server.

It has some basic configuration like
```python
CHANNEL_ID = 0 # ID of the discord channel
MESSAGE_ID = 0 # ID of the message
SERVER_ADDRESS = "localhost" # Adress of the minecraft server
START_COMMAND = "./start.sh" # Bash script to start the server
STOP_COMMAND = "./stop.sh" # Bash script to stop the server
EMOJI = "👍" # The emoji to look for
EMOJI_LIMIT = 1 # The number of emojis to start the server -1 because I forgot to change the code
```
