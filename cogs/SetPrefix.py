from discord.ext import commands
import discord
import myBot
from discord.commands import Option,slash_command

class SetPrefix(commands.Cog):
 def __init__(self,client):
  self.client=client
 @commands.command(aliases=["sp"])
 async def setprefix(self,ctx,prefix:str):
   myBot.cursor.execute(f"UPDATE guildIds SET prefix='{prefix}' WHERE guildId = {ctx.guild.id};")
   myBot.db.commit()
   await ctx.send(embed=discord.Embed(title=f"Successfully set prefix to `{prefix}`",color = discord.Color.green()))
 @slash_command(name="setprefix",description="Set custom prefix for your server")
 async def setprefix(self,ctx,prefix:Option(str,"Prefix to set",default = None, required=True)):
   await ctx.defer()
   myBot.cursor.execute(f"UPDATE guildIds SET prefix='{prefix}' WHERE guildId = {ctx.guild.id};")
   myBot.db.commit()
   await ctx.respond(embed=discord.Embed(title=f"Successfully set prefix to `{prefix}`",color = discord.Color.green()))


def setup(client):
 client.add_cog(SetPrefix(client))