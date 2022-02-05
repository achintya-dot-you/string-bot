from discord.ext import commands
import discord
import random
from cogs.Beg import Beg
import myBot
import math
from discord.commands import Option,slash_command

class Ping(commands.Cog):
 def __init__(self,client) -> None:
     self.client=client
 @slash_command(description="Returns the bot's ping")
 async def ping(self,ctx):
   await ctx.defer()
   embed = discord.Embed(title=f" :electric_plug: :regional_indicator_p::regional_indicator_i::regional_indicator_n::regional_indicator_g: :regional_indicator_i::regional_indicator_s:  {math.trunc((self.client.latency)*1000)}ms :electric_plug: ",color=discord.Colour.green())
   await ctx.respond(embed=embed)
   myBot.increaseCommandsUsed(ctx.author.id,ctx.author)
 @commands.command()
 async def ping(self,ctx):
  embed = discord.Embed(title=f" :electric_plug: :regional_indicator_p::regional_indicator_i::regional_indicator_n::regional_indicator_g: :regional_indicator_i::regional_indicator_s:   {math.trunc((self.client.latency)*1000)}ms :electric_plug: ",color=discord.Colour.green())
  await ctx.send(embed=embed)


def setup(client):
 client.add_cog(Ping(client))