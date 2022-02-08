from pypresence import Presence
import time

start_time = time.time()
client_id = "931237127650426911"
rpc = Presence(client_id)
rpc.connect()
rpc.update(state="writing code", details="Coding String Bot.", large_image="string", buttons=[{"label":"get my dumb bot", "url":"https://discord.com/api/oauth2/authorize?client_id=939185469315489853&permissions=8&scope=bot%20applications.commands"}, {"label":"don't copy the code lmaoo", "url":"https://www.github.com/achintya-dot-you/string-bot"}], start=start_time)

while True:
 rpc.update(state="writing code", details="Coding String Bot.", large_image="string", buttons=[{"label":"get my dumb bot", "url":"https://discord.com/api/oauth2/authorize?client_id=939185469315489853&permissions=8&scope=bot%20applications.commands"}, {"label":"don't copy the code lmaoo", "url":"https://www.github.com/achintya-dot-you/string-bot"}], start=start_time)