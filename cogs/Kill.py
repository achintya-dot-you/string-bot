from discord.ext import commands
import discord
import random
import myBot
from discord.commands import Option,slash_command
kill_reasons = ["went broke and died....","never knew about Reddit, died of boredom...", "fell off a cliff and died....",
"got the corona and died(here's your reminder to get vaccinated :D)", "went on a road trip in a storm and died...", 
"had a high ping in Fortnite and banged their head on the wall, only to discover they had brain cancer and died.",
"got bro-zoned :d","used anime powers, just to kill themselves." ]
class Kill(commands.Cog):
 def __init__(self,client):
  self.client=client
 @slash_command(name="kill",description="People die, no biggie :D")
 async def kill1(self,ctx, member : Option(discord.Member , "Person whom you wanna kill ", required=True,default=None)):
   await ctx.defer()
   if member ==None:
     await ctx.send("You need to specify a member, *genius*!")
   
   
   else:
     author=ctx.author  
     if member==author:
       await ctx.respond("No suicide bro.") 
       return
     elif member.id==self.client.user.id:
       await ctx.respond("**Nope, you ain't gon' kill me** ")
       return
   
     reason = random.choice(kill_reasons)
     newEmbed = discord.Embed(title="", description=f'<@!{member.id}> {reason}',colour = discord.Colour.random())
     avatar = author.avatar
     if avatar == None:
       newEmbed.set_footer(text=f'{author} wanted to kill you ig',icon_url = author.display_avatar)
     elif avatar != None:
       newEmbed.set_footer(text=f'{author} wanted to kill you ig',icon_url=avatar)
     await ctx.respond(embed=newEmbed)
     myBot.increaseCommandsUsed(ctx.author.id, ctx.author)

 @commands.command()
 async def kill(self,ctx, member:discord.Member=None):
   if member ==None:
     await ctx.send("You need to specify a member, *genius*!")
   else:
     author=ctx.author  
     if member==author:
       await ctx.send("No suicide bro.") 
       return
     elif member.id==self.client.user.id:
       await ctx.send("**Nope, you ain't gon' kill me** ")
       return
   
     reason = random.choice(kill_reasons)
     newEmbed = discord.Embed(title="", description=f'<@{member.id}> {reason}',colour = discord.Colour.random())
     newEmbed.set_footer(text=f'{author} wanted to kill you ig',icon_url=author.avatar)
     await ctx.send(embed=newEmbed)

def setup(client):
 client.add_cog(Kill(client))