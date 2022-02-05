from discord.ext import commands
import discord
import myBot
from discord.commands import Option,slash_command
class Gift(commands.Cog):
 def __init__(self,client):
  self.client=client

 @slash_command(name="gift",description="Gift another user some of your sweet money <3")
 async def gift1(self,ctx, member:Option(discord.Member, "Person whom you wanna give your money ", default = None, required=True), amount:Option(int,"Number of coins to give", required=True, default = None)):
   await ctx.defer()
   myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000, 0) ON DUPLICATE KEY UPDATE balance = balance;")
   myBot.db.commit()
   myBot.cursor.execute(f"SELECT balance FROM economy WHERE user_id={ctx.author.id};")
   balance = myBot.cursor.fetchone()
   if amount>balance[0]:
     embed = discord.Embed(title="You don't have enough money lol", color = discord.Color.red())
     await ctx.respond(embed=embed)
     return
   elif amount<1:
     embed = discord.Embed(title="Nope, you can't gift that.", color = discord.Color.red())
     await ctx.respond(embed=embed)
     return
   else:
     myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000-{amount}, 1) ON DUPLICATE KEY UPDATE balance = balance-{amount};  ")
     myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({member.id},'{member}', 1000+{int(0.95*amount)}, 0) ON DUPLICATE KEY UPDATE balance = balance+{int(0.95*amount)};")
     myBot.db.commit()
     embed = discord.Embed(title=f'{ctx.author} gifted to {member}', description= f"Successfully gifted **{int(0.95*amount)}** to {member.mention} ", color = discord.Colour.green())
     embed.set_footer(text = f"5%  ({int(amount * 0.05)} coins) tax was deducted. To trade tax-free, get PREMIUM", icon_url=self.client.user.display_avatar)
     await ctx.respond(embed=embed)
     myBot.increaseCommandsUsed(ctx.author.id, ctx.author)
 @commands.command()
 async def gift(self,ctx,member:discord.Member = None,amount:int = None):
  if member==None:
   await ctx.send("**Wooohooo, we ain't mentioning people to give money today!**")
   return
  if amount==None:
   await ctx.send("**Mmhm, lemme send nothing to them.**")
   return
  myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000, 0) ON DUPLICATE KEY UPDATE balance = balance;")
  myBot.db.commit()
  myBot.cursor.execute(f"SELECT balance FROM economy WHERE user_id={ctx.author.id};")
  balance = myBot.cursor.fetchone()
  if amount>balance[0]:
     embed = discord.Embed(title="You don't have enough money lol", color = discord.Color.red())
     await ctx.send(embed=embed)
     return
  elif amount<1:
     embed = discord.Embed(title="Nope, you can't gift that.", color = discord.Color.red())
     await ctx.send(embed=embed)
     return
  else:
     myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({ctx.author.id},'{ctx.author}', 1000-{amount}, 1) ON DUPLICATE KEY UPDATE balance = balance-{amount};  ")
     myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used) VALUES ({member.id},'{member}', 1000+{int(0.95*amount)}, 0) ON DUPLICATE KEY UPDATE balance = balance+{int(0.95*amount)};")
     myBot.db.commit()
     embed = discord.Embed(title=f'{ctx.author} gifted to {member}', description= f"Successfully gifted **{int(0.95*amount)}** to {member.mention} ", color = discord.Colour.green())
     embed.set_footer(text = f"5%  ({int(amount * 0.05)} coins) tax was deducted. To trade tax-free, get PREMIUM", icon_url=self.client.user.display_avatar)
     await ctx.send(embed=embed)
     myBot.increaseCommandsUsed(ctx.author.id, ctx.author)


def setup(client):
 client.add_cog(Gift(client))