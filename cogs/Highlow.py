from discord.ext import commands
import discord
import myBot
import random
from discord.commands import Option,slash_command
difficultyMeter = {"Very Easy":51,"Easy":101,"Medium":501,"Hard":1001,"Very Hard":5001}
def GiveNumber(difficulty):
 number=random.randrange(1,difficultyMeter[difficulty])
 return number
class MyView(discord.ui.View):
 def __init__(self, ctx,difficulty,randomNumber):
  super().__init__(timeout=35)
  self.ctx=ctx
  self.numberToGuess = GiveNumber(difficulty)
  self.randomNumber = randomNumber
 @discord.ui.button(emoji="🔼",style=discord.ButtonStyle.primary)
 async def buttoncallback1(self,button,interaction):
  if self.numberToGuess>self.randomNumber:
   await interaction.response.edit_message(embed=discord.Embed(title="You have won!",description=f"Congratulations, you have won, the number I was thinking of was: **{self.numberToGuess}**",color=discord.Color.green()),view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  else:
   await interaction.response.edit_message(embed=discord.Embed(title="You have lost :(",description=f"Oh no, you have lost, the number I was thinking of was: **{self.numberToGuess}**",color=discord.Color.red()),view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
 @discord.ui.button(emoji="🔽",style=discord.ButtonStyle.primary)
 async def buttoncallback(self,button,interaction):
  if self.numberToGuess<self.randomNumber:
   await interaction.response.edit_message(embed=discord.Embed(title="You have won!",description=f"Congratulations, you have won, the number I was thinking of was: **{self.numberToGuess}**",color=discord.Color.green()),view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  else:
   await interaction.response.edit_message(embed=discord.Embed(title="You have lost :(",description=f"Oh no, you have lost, the number I was thinking of was: **{self.numberToGuess}**",color=discord.Color.red()),view=None) 
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
 @discord.ui.button(emoji="⏸",style=discord.ButtonStyle.primary)
 async def buttoncallback2(self,button,interaction):
  if self.numberToGuess==self.randomNumber:
   await interaction.response.edit_message(embed=discord.Embed(title="You have won!",description=f"Congratulations, you have won, the number I was thinking of was: **{self.numberToGuess}**",color=discord.Color.green()),view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  else:
   await interaction.response.edit_message(embed=discord.Embed(title="You have lost :(",description=f"Oh no, you have lost, the number I was thinking of was: **{self.numberToGuess}**",color=discord.Color.red()),view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)

     


class Highlow(commands.Cog):
 def __init__(self,client):
     self.client=client
 @slash_command(name="highlow",description="Play a game of number guessing with the bot")
 async def highlow1(self,ctx,difficulty:Option(str,"Enter difficulty level:", default=None, required=True,choices = ["Very Easy","Easy","Medium","Hard","Very Hard"])):
  await ctx.defer()
  number=random.randrange(1,difficultyMeter[difficulty])
  view=MyView(ctx,difficulty,number)
  embed=discord.Embed(title=f"{ctx.author}'s Highlow game",description=f"I have picked a number between **1 and {int(difficultyMeter[difficulty])-1}**. \n Is it above, below, or equal to **{number}**.",color=discord.Color.purple())
  await ctx.respond(embed=embed,view=view)
 @commands.command(aliases=["hl"])
 async def highlow(self,ctx,difficulty):
  number=random.randrange(1,difficultyMeter[difficulty])
  view=MyView(ctx,difficulty,number)
  embed=discord.Embed(title=f"{ctx.author}'s Highlow game",description=f"I have picked a number between **1 and {int(difficultyMeter[difficulty])-1}**. \n Is it above, below, or equal to **{number}**.",color=discord.Color.purple())
  await ctx.send(embed=embed,view=view)



def setup(client):
 client.add_cog(Highlow(client))