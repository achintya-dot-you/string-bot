from turtle import color
from discord.ext import commands
import discord
import random
import myBot
from discord.commands import Option,slash_command

class Clear(commands.Cog):
 def __init__(self,client):
    self.client = client
 @commands.command()
 async def clear(self,ctx, amount=20):
  await ctx.channel.purge(limit=amount)
  await ctx.send(embed=discord.Embed(title=f"Successfully cleared {amount} messages!",color = discord.Color.green()))
 @slash_command(name="clear",description="Helps you clear server messages!")
 async def clear1(self,ctx, amount=20):
  await ctx.defer()
  await ctx.channel.purge(limit=int(amount))
  await ctx.send(f'Clearing {amount} messages!')
  myBot.increaseCommandsUsed(ctx.author.id,ctx.author)


def setup(client):
   client.add_cog(Clear(client))