from click import BadArgumentUsage
from discord.ext import commands
import discord
import myBot
import discord.ext
from discord.commands import Option,slash_command

class Leaderboard(commands.Cog):
 def __init__(self,client):
  self.client=client
 @slash_command(name="leaderboard",description="Get the leaderboard for various categories")
 async def leaderboard1(self,ctx,category:Option(str, "Category for leaderboard", required= True, choices = ["Cricket Score","Commands Used","Money","RPS Won"]), top: Option(int, "How many top entries", required = False, default = 10, choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])):
    await ctx.defer()
    if category == "Cricket Score":
      aaaa=""
      bbbb=""
      myBot.cursor.execute(f"SELECT username,highest_score FROM economy ORDER BY highest_score DESC LIMIT {top};")
      abc=myBot.cursor.fetchall()
      if len(abc) < top :
        top = len(abc)
      for i in range(0,top):
        aaaa = str(aaaa + str(abc[i][0]))+"\n"
        bbbb = str(bbbb + str(abc[i][1]))+"\n"
    
      embed = discord.Embed(title=f"Top {top} users according to their cricket score.", color = discord.Color.purple())
      embed.add_field(name="Username", value=f"{aaaa}",inline=True)
      embed.add_field(name="Highest Score",value=f"{bbbb}",inline = True)
      embed.set_footer(text="pretty epic i'd say")
      await ctx.respond(embed=embed)
    elif category == "Commands Used":
      aaaa=""
      bbbb=""
      myBot.cursor.execute(f"SELECT username,commands_used FROM economy ORDER BY commands_used DESC LIMIT {top};")
      abc=myBot.cursor.fetchall()
      if len(abc) < top :
        top = len(abc)
      for i in range(0,top):
        aaaa = str(aaaa + str(abc[i][0]))+"\n"
        bbbb = str(bbbb + str(abc[i][1]))+"\n"
    
      embed = discord.Embed(title=f"Top {top} users according to their commands used.", color = discord.Color.purple())
      embed.add_field(name="Username", value=f"{aaaa}",inline=True)
      embed.add_field(name="Commands Used",value=f"{bbbb}",inline = True)
      embed.set_footer(text="the goats lmao")
      await ctx.respond(embed=embed)
    elif category == "Money":
      aaaa=""
      bbbb=""
      myBot.cursor.execute(f"SELECT username,balance FROM economy ORDER BY balance DESC LIMIT {top};")
      abc=myBot.cursor.fetchall()
      if len(abc) < top :
        top = len(abc)
      for i in range(0,top):
        aaaa = str(aaaa + str(abc[i][0]))+"\n"
        bbbb = str(bbbb + str(abc[i][1]))+"\n"
    
      embed = discord.Embed(title=f"Top {top} users according to their money.", color = discord.Color.purple())
      embed.add_field(name="Username", value=f"{aaaa}",inline=True)
      embed.add_field(name="Money",value=f"{bbbb}",inline = True)
      embed.set_footer(text="cool gamer.")
      await ctx.respond(embed=embed)
    elif category == "RPS Won":
      aaaa=""
      bbbb=""
      myBot.cursor.execute(f"SELECT username,rps_won FROM economy ORDER BY rps_won DESC LIMIT {top};")
      abc=myBot.cursor.fetchall()
      if len(abc) < top :
        top = len(abc)
      for i in range(0,top):
        aaaa = str(aaaa + str(abc[i][0]))+"\n"
        bbbb = str(bbbb + str(abc[i][1]))+"\n"
    
      embed = discord.Embed(title=f"Top {top} users according to their Rock Paper Scissors won.", color = discord.Color.purple())
      embed.add_field(name="Username", value=f"{aaaa}",inline=True)
      embed.add_field(name="Times Won",value=f"{bbbb}",inline = True)
      embed.set_footer(text="pro.")
      await ctx.respond(embed=embed)


    myBot.increaseCommandsUsed(ctx.author.id,ctx.author)
 
 @commands.command(aliases=['lb'])
 async def leaderboard(self,ctx,category:str=None,top:int=10):
  try:
    if category == "Cricket Score" or category == "cs" or category == "CS" or category=="cricketscore" or category == "cricket score" or category == "Cs":
      aaaa=""
      bbbb=""
      myBot.cursor.execute(f"SELECT username,highest_score FROM economy ORDER BY highest_score DESC LIMIT {top};")
      abc=myBot.cursor.fetchall()
      if len(abc) < top :
        top = len(abc)
      for i in range(0,top):
        aaaa = str(aaaa + str(abc[i][0]))+"\n"
        bbbb = str(bbbb + str(abc[i][1]))+"\n"
    
      embed = discord.Embed(title=f"Top {top} users according to their cricket score.", color = discord.Color.purple())
      embed.add_field(name="Username", value=f"{aaaa}",inline=True)
      embed.add_field(name="Highest Score",value=f"{bbbb}",inline = True)
      embed.set_footer(text="pretty epic i'd say")
      await ctx.send(embed=embed)
      return
    elif category == "Commands Used" or category =="commands used" or category == "cu" or category == "Cu" or category == "CU":
        aaaa=""
        bbbb=""
        myBot.cursor.execute(f"SELECT username,commands_used FROM economy ORDER BY commands_used DESC LIMIT {top};")
        abc=myBot.cursor.fetchall()
        if len(abc) < top :
          top = len(abc)
        for i in range(0,top):
          aaaa = str(aaaa + str(abc[i][0]))+"\n"
          bbbb = str(bbbb + str(abc[i][1]))+"\n"
      
        embed = discord.Embed(title=f"Top {top} users according to their commands used.", color = discord.Color.purple())
        embed.add_field(name="Username", value=f"{aaaa}",inline=True)
        embed.add_field(name="Commands Used",value=f"{bbbb}",inline = True)
        embed.set_footer(text="the goats lmao")
        await ctx.send(embed=embed)
        return
    else:
     await ctx.send('**not a valid category lol. Current Categories are: ** \n 1.Cricket Score(cs) \n 2.Commands Used(cu)')
  except BadArgumentUsage:
    await ctx.send("yo i think you messed up an argument. Here's how you do it - `lb <category> <top entries(optional)>`")



def setup(client):
 client.add_cog(Leaderboard(client))
