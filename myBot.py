import dotenv
dotenv.load_dotenv()
import math
from tkinter.messagebox import YES
import mysql.connector
from datetime import datetime
import os
from email import message
from pydoc import describe
from re import purge
import discord
from discord.ui import Button, View
import random
from discord.ext import commands, tasks
from discord.commands import Option
import discord.ext

db = mysql.connector.connect(
 host="34.93.32.224",
 user="root",
 passwd=os.environ["passwd"],
 database="testdatabase"
)
cursor=db.cursor()
async def get_prefix(client, message):
    try:
        cursor.execute(f"SELECT prefix FROM guildIds WHERE guildId = {message.guild.id};")
        abc=cursor.fetchone()
        prefix=abc[0]
        return prefix
    except Exception:
        return "=="
client = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all(), debug_guilds = [816334274545319996,763348615233667082,884279584659476511])
client.remove_command("help")

@client.command()
async def help(ctx):
  try:
    await ctx.author.send("Bro u know me?")
  except discord.HTTPException:
    await ctx.send("Bro u know me?")


#---------------------------FUNCTIONS--------------------------------
def increaseCommandsUsed(userid, username):
 cursor.execute(f"INSERT INTO economy (user_id,username, balance, commands_used, fc) VALUES ({userid},'{username}',1000,1, 0) ON DUPLICATE KEY UPDATE commands_used = commands_used+1;")
 db.commit()
#----------------------FUN COMMANDS -------------

#------RUN STUFF -------
lst = [f for f in os.listdir("cogs/") if os.path.isfile(os.path.join("cogs/", f))]
no_py = [s.replace('.py', '') for s in lst]
startup_extensions = ["cogs." + no_py for no_py in no_py]
try:
  for cogs in startup_extensions:
    client.load_extension(cogs)  # Startup all cogs

    print(f"Loaded {cogs}")

except Exception as getgood:
  print(getgood)

client.run("OTM5MTg1NDY5MzE1NDg5ODUz.Yf1KoQ.Bm-0x6y3A0Sx-RCExmnp6RmxdF4")