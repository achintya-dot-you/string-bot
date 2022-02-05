from aiohttp import ClientError
from discord.ext import commands
import discord
import random
import myBot
from discord.commands import Option,slash_command

class Beg(commands.Cog):
 def __init__(self,client) -> None:
  self.client=client
 @commands.command()
 async def beg(self,ctx):
   randMoney = random.randrange(0,1001)
   myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000+{randMoney}, 1) ON DUPLICATE KEY UPDATE balance = balance+{randMoney};")
   myBot.db.commit()
   await ctx.send(f"Someone gave <@!{ctx.author.id}> {randMoney} coins")
 @slash_command(name="beg",description="Beg some coins and get rich :D")
 async def beg(self,ctx):
  await ctx.defer()
  randMoney = random.randrange(0,1001)
  myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000+{randMoney}, 1) ON DUPLICATE KEY UPDATE balance = balance+{randMoney};")
  myBot.db.commit()
  await ctx.respond(f"Someone gave <@!{ctx.author.id}> {randMoney} coins")


def setup(client):
 client.add_cog(Beg(client))