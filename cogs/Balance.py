from discord.ext import commands
import discord
import random
import myBot
from discord.commands import Option,slash_command

class Balance(commands.Cog):
 def __init__(self,client):
    self.client=client
 @commands.command(aliases=["bal"])
 async def balance(self,ctx, member:discord.Member=None):
  if member==None:
    myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000, 0) ON DUPLICATE KEY UPDATE balance = balance;")
    myBot.db.commit()
    myBot.cursor.execute(f"SELECT balance FROM economy WHERE user_id={ctx.author.id};")
    balance = myBot.cursor.fetchone()
    await ctx.send(embed=discord.Embed(title=f"Your balance is {balance[0]}.",color=discord.Color.nitro_pink()))
  elif member != None:
    myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({member.id},'{member}', 1000, 0) ON DUPLICATE KEY UPDATE balance = balance;")
    myBot.db.commit()
    myBot.cursor.execute(f"SELECT balance FROM economy WHERE user_id={member.id};")
    balance = myBot.cursor.fetchone()
    await ctx.send(embed=discord.Embed(title=f"{member}'s balance is {balance[0]}.",color=discord.Color.nitro_pink()))
 @slash_command(name="balance",description="Tells you your or someone else's balance")
 async def balance1(self,ctx,member:Option(discord.Member,"Member to get the balance from",required=False,default=None)):
  await ctx.defer()
  if member==None:
    myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000, 0) ON DUPLICATE KEY UPDATE balance = balance;")
    myBot.db.commit()
    myBot.cursor.execute(f"SELECT balance FROM economy WHERE user_id={ctx.author.id};")
    balance = myBot.cursor.fetchone()
    await ctx.respond(embed=discord.Embed(title=f"Your balance is {balance[0]}.",color=discord.Color.nitro_pink()))
  elif member != None:
    myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({member.id},'{member}', 1000, 0) ON DUPLICATE KEY UPDATE balance = balance;")
    myBot.db.commit()
    myBot.cursor.execute(f"SELECT balance FROM economy WHERE user_id={member.id};")
    balance = myBot.cursor.fetchone()
    await ctx.respond(embed=discord.Embed(title=f"{member}'s balance is {balance[0]}.",color=discord.Color.nitro_pink()))

  myBot.increaseCommandsUsed(ctx.author.id,ctx.author)


def setup(client):
 client.add_cog(Balance(client))