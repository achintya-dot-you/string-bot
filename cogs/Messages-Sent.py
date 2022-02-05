from discord.ext import commands
import discord
import myBot
from discord.commands import Option,slash_command

class MessagesSent(commands.Cog):
 def __init__(self,client):
  self.client=client
 @slash_command(description = "Check how many messages you have sent in this server", name="messages-sent")
 async def messagessent(self,ctx, member : Option(discord.Member, "Check another person's messages sent", required=False, default=None)):
   await ctx.defer()
   if member==None:
     myBot.cursor.execute(f"INSERT INTO a{ctx.guild.id} (user_id, username, messages_sent) VALUES ({ctx.author.id},'{ctx.author}', 0) ON DUPLICATE KEY UPDATE messages_sent = messages_sent;")
     myBot.db.commit()
     myBot.cursor.execute(f"SELECT messages_sent FROM a{ctx.guild.id} WHERE user_id={ctx.author.id};")
     sm = myBot.cursor.fetchone()
     embed = discord.Embed(title = f"You have sent {sm[0]} messages in this server", color = discord.Colour.green())
     await ctx.respond(embed=embed)
     myBot.increaseCommandsUsed(ctx.author.id,ctx.author)
   elif member.id == self.client.user.id:
     embed=discord.Embed(title=f"I have", description = "** sent more messages than you have seen in your entire life lol**", color = discord.Colour.purple())
     embed.set_footer(text="lmao")
     await ctx.respond(embed=embed)
     myBot.increaseCommandsUsed(ctx.author.id,ctx.author)
     return
   else:
     myBot.cursor.execute(f"INSERT INTO a{ctx.guild.id} (user_id, username, messages_sent) VALUES ({member.id},'{member}', 0) ON DUPLICATE KEY UPDATE messages_sent = messages_sent;")
     myBot.db.commit()
     myBot.cursor.execute(f"SELECT messages_sent FROM a{ctx.guild.id} WHERE user_id={member.id};")
     sm = myBot.cursor.fetchone()
     embed = discord.Embed(title = f"{member.name} has sent {sm[0]} messages in this server", color = discord.Colour.green())
     await ctx.respond(embed=embed)
     myBot.increaseCommandsUsed(ctx.author.id, ctx.author)
 @commands.command(aliases=['sm'])
 async def messagessent(self,ctx,member:discord.Member=None):
  if member==None:
     myBot.cursor.execute(f"INSERT INTO a{ctx.guild.id} (user_id, username, messages_sent) VALUES ({ctx.author.id},'{ctx.author}', 0) ON DUPLICATE KEY UPDATE messages_sent = messages_sent;")
     myBot.db.commit()
     myBot.cursor.execute(f"SELECT messages_sent FROM a{ctx.guild.id} WHERE user_id={ctx.author.id};")
     sm = myBot.cursor.fetchone()
     embed = discord.Embed(title = f"You have sent {sm[0]} messages in this server", color = discord.Colour.green())
     await ctx.send(embed=embed)
  elif member.id == self.client.user.id:
      embed=discord.Embed(title=f"I have", description = "** sent more messages than you have seen in your entire life lol**", color = discord.Colour.purple())
      embed.set_footer(text="lmao")
      await ctx.send(embed=embed)
      return
  else:
     myBot.cursor.execute(f"INSERT INTO a{ctx.guild.id} (user_id, username, messages_sent) VALUES ({member.id},'{member}', 0) ON DUPLICATE KEY UPDATE messages_sent = messages_sent;")
     myBot.db.commit()
     myBot.cursor.execute(f"SELECT messages_sent FROM a{ctx.guild.id} WHERE user_id={member.id};")
     sm = myBot.cursor.fetchone()
     embed = discord.Embed(title = f"{member.name} has sent {sm[0]} messages in this server", color = discord.Colour.green())
     await ctx.send(embed=embed)


def setup(client):
 client.add_cog(MessagesSent(client))