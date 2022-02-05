from discord.ext import commands
import discord
import myBot
from discord.commands import Option,slash_command


class BanKick(commands.Cog):
 def __init__(self,client):
     self.client = client
 @slash_command(name="ban",description="Ban people(only works with mod perms)")
 async def ban1(self,ctx,member:Option(discord.Member,"Member to ban",required=True), reason:Option(str,"Reason to ban the member",default = "No reason provided", required = False)):
   await ctx.defer()
   smolMember=member
   try:
     try:
       await smolMember.send(f'You were **banned** by **{ctx.author}** in **{ ctx.guild.name}** because *{reason}*.')
     except Exception:pass
     await member.kick()
     await ctx.respond(f'{smolMember} was banned.')
     myBot.increaseCommandsUsed(ctx.author.id,ctx.author)
   except Exception:
     embed=discord.Embed(title="lol u need perms :smirk:",description="imagine thinking that you can ban people", color = discord.Colour.red())
     await ctx.respond(embed=embed)
     return

 @slash_command(name="kick",description="Kicks a member(only works with mod perms)")
 async def kick1(self,ctx,member:Option(discord.Member, "Member to be kicked " ,required=True, default=None), reason:Option(str, "Reason to kick the member.", default="No reason provided", required=False)):
    await ctx.defer()
    smolMember=member
    try:
      try:
        link = await ctx.channel.create_invite(max_age=0)
        await smolMember.send(f'You were **kicked** by **{ctx.author}** in **{ ctx.guild.name}** because *{reason}*. **Join again** : {link}')
      except Exception:pass
      await member.kick()
      await ctx.respond(f'{smolMember} was kicked.')
      myBot.increaseCommandsUsed(ctx.author.id,ctx.author)
    except Exception:
      embed=discord.Embed(title="lol u need perms :smirk:",description="imagine thinking that you can kick people", color = discord.Colour.red())
      await ctx.respond(embed=embed)
      return
 @commands.command(aliases=['k'])
 async def kick(self,ctx,member:discord.Member=None, reason:str="No reason provided"):
     smolMember=member
     if member==None:
      await ctx.send("**You need to specify a member :p**")
      return
     try:
       try:
         link = await ctx.channel.create_invite(max_age=0)
         await smolMember.send(f'You were **kicked** by **{ctx.author}** in **{ ctx.guild.name}** because *{reason}*. **Join again** : {link}')
       except Exception:pass
       await member.kick()
       await ctx.send(f'{smolMember} was kicked.')
     except Exception:
       embed=discord.Embed(title="lol u need perms :smirk:",description="imagine thinking that you can kick people", color = discord.Colour.red())
       await ctx.send(embed=embed)
       return
 @commands.command(aliases=['b'])
 async def ban(self,ctx,member:discord.Member, reason="No reason provided"):
  smolMember=member
  if member==None:
   await ctx.send("**You need to specify a member :p**")
   return
  try:
       try:
           await smolMember.send(f'You were **banned** by **{ctx.author}** in **{ ctx.guild.name}** because *{reason}*.')
       except Exception:pass
       await member.ban()
       await ctx.send(f'{smolMember} was banned.')
  except Exception:
       embed=discord.Embed(title="lol u need perms :smirk:",description="imagine thinking that you can ban people", color = discord.Colour.red())
       await ctx.send(embed=embed)
       return


def setup(client):
 client.add_cog(BanKick(client))