# Discord Bot for managing Minecraft Servers
This bot checks for react emoji on a certain discord message, if they are enough of x emoji (check script) it starts the server. It also stops the server automatically.

It has some basic configuration:
```python
CHANNEL_ID = 0
MESSAGE_ID = 0
TOKEN = open("TOKEN", "r").read()
START_COMMAND = "./start.sh"
server = JavaServer.lookup("localhost", 25565)
