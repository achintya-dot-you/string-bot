from multiprocessing.connection import Client
from unicodedata import numeric
from discord.ext import commands
import discord
import myBot
import random
from discord.commands import Option,slash_command
difficultyMeter = {"Very Easy":51,"Easy":101,"Medium":501,"Hard":1001,"Very Hard":5001}
async def getMessage(difficulty,ctx,client,winningNumber,tries):

 def check(m):
    return m.channel == ctx.channel and m.author == ctx.author
 
 message =await  client.wait_for("message",timeout=100,check=check)
 await checkIfWon(difficulty,winningNumber,message,ctx,client,tries)
 return
async def checkIfWon(difficulty,winningNum,message,ctx,client,tries):
    hintsLeft = 2
    randomNumber = random.randrange(1,difficultyMeter[difficulty])
    tries=tries
    if randomNumber==winningNum:
     randomNumber+=1
    if message.content==str(winningNum):
     tries+=1
     await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in {tries} tries",color=discord.Color.green()))
     return
    elif message.content == "hint" or message.content=="h" or message.content=="Hint":
     if hintsLeft==0:
      await ctx.send(embed=discord.Embed(title=f"You have exhausted all hints, no hints left. Guess the number",color=discord.Color.dark_purple()))
      await getMessage(difficulty,ctx,client,winningNum,tries)
     if randomNumber>winningNum:
      await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}**. Guess the number ",color=discord.Color.dark_purple()))
      hintsLeft-=1
      await getMessage(difficulty,ctx,client,winningNum,tries)
     elif randomNumber<winningNum:
      await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** Guess the number ",color=discord.Color.purple()))
      hintsLeft-=1
      await getMessage(difficulty,ctx,client,winningNum,tries)
    else:
     tries+=1
     await ctx.send(embed=discord.Embed(title=f"No, thats not the number. Try again. You have done {tries} tries till now"))
     await getMessage(difficulty,ctx,client,winningNum,tries)



  

class Guessthenumber(commands.Cog):
 def __init__(self,client):
     self.client=client
     self.tries=0
     self.triesLeft = 5
 @commands.command(aliases=["gtn"])
 async def guessthenumber(self,ctx,*,difficulty:str=None):
  if difficulty=="very easy" or difficulty=="ve" or difficulty=="Ve" or difficulty=="Very easy" or difficulty=="Very Easy": 
   winningNumber=random.randint(1,difficultyMeter["Very Easy"])
   difficulty="Very Easy"
  elif difficulty=="easy" or difficulty=="e" or difficulty=="E" or difficulty=="Easy": 
   winningNumber=random.randint(1,difficultyMeter["Easy"])
   difficulty="Easy"
  elif difficulty=="medium" or difficulty=="m" or difficulty=="M" or difficulty=="Medium": 
   winningNumber=random.randint(1,difficultyMeter["Medium"])
   difficulty="Medium"
  elif difficulty=="hard" or difficulty=="h" or difficulty=="H" or difficulty=="Hard": 
   winningNumber=random.randint(1,difficultyMeter["Hard"])
   difficulty="Hard"
  elif difficulty=="very hard" or difficulty=="vh" or difficulty=="Vh" or difficulty=="Very hard" or difficulty=="Very Hard": 
   winningNumber=random.randint(1,difficultyMeter["Very Hard"])
   difficulty="Very Hard"
  else:
   await ctx.send("Not a valid difficulty level. Difficulty levels are : \n **1.Very Easy(ve)** \n **2.Easy(e)**\n**3.Medium(m)**\n**4.Hard(h)**\n**5.Very Hard(vh)**")
   return

  await ctx.send(embed=discord.Embed(title=f"{ctx.author}'s Guess the Number game.",description=f"THE GAME OF GUESS THE NUMBER IS NOW STARTING \n I HAVE PICKED A NUMBER **BETWEEN 1 AND {int(difficultyMeter[difficulty])-1}** \n **GUESS THE NUMBER!**",color=discord.Color.nitro_pink()))
  await getMessage(difficulty,ctx,self.client,winningNumber,self.tries)
 @slash_command(name="guessthenumber",description="Play a game of gtn with the bot!")
 async def guessthenumber1(self,ctx,difficulty:Option(str,"Enter difficulty level:", default=None, required=True,choices = ["Very Easy","Easy","Medium","Hard","Very Hard"])):
  winningNumber=random.randint(1,difficultyMeter[difficulty])
  await ctx.respond(embed=discord.Embed(title=f"{ctx.author}'s Guess the Number game.",description=f"THE GAME OF GUESS THE NUMBER IS NOW STARTING \n I HAVE PICKED A NUMBER **BETWEEN 1 AND {int(difficultyMeter[difficulty])-1}** \n **GUESS THE NUMBER!**",color=discord.Color.nitro_pink()))
  await getMessage(difficulty,ctx,self.client,winningNumber,self.tries)



def setup(client):
 client.add_cog(Guessthenumber(client))

































'''
  if returnMessage(ctx,self.client) == str(number):
   await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in 1 try",color=discord.Color.green()))
   return
  elif returnMessage(ctx,self.client) == "hint" or returnMessage(ctx,self.client) == "Hint" or returnMessage(ctx,self.client) == "h":
   if randomNumber>number:
    await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}** ",color=discord.Color.dark_purple()))
   elif randomNumber<number:
    await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** ",color=discord.Color.purple()))
  else:
   self.triesLeft=self.triesLeft-1
   if self.triesLeft==0:
    await ctx.send(embed=discord.Embed(title=f"All your tries have been exhausted. YOU HAVE LOST THE GAME",color=discord.Color.red()))
    return
   else:
    await ctx.send(embed=discord.Embed(title="That was not the number, you have 4 tries left!.",description="**GUESS THE NUMBER AGAIN, OR TAKE A HINT**",color=discord.Color.red()))
    if returnMessage(ctx,self.client) == str(number):
     await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in 2 tries",color=discord.Color.green()))
     return
    elif returnMessage(ctx,self.client) == "hint" or returnMessage(ctx,self.client) == "Hint" or returnMessage(ctx,self.client) == "h":
     if randomNumber>number:
      await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}** ",color=discord.Color.dark_purple()))
     elif randomNumber<number:
      await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** ",color=discord.Color.purple()))
    else:
     self.triesLeft=self.triesLeft-1
     if self.triesLeft==0:
      await ctx.send(embed=discord.Embed(title=f"All your tries have been exhausted. YOU HAVE LOST THE GAME",color=discord.Color.red()))
      return
     else:
      await ctx.send(embed=discord.Embed(title="That was not the number, you have 3 tries left!.",description="**GUESS THE NUMBER AGAIN, OR TAKE A HINT**",color=discord.Color.red()))
      if returnMessage(ctx,self.client) == str(number):
       await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in 3 tries",color=discord.Color.green()))
       return
      elif returnMessage(ctx,self.client) == "hint" or returnMessage(ctx,self.client) == "Hint" or returnMessage(ctx,self.client) == "h":
       if randomNumber>number:
        await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}** ",color=discord.Color.dark_purple()))
       elif randomNumber<number:
        await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** ",color=discord.Color.purple())) 
      else:
        self.triesLeft=self.triesLeft-1
        if self.triesLeft==0:
         await ctx.send(embed=discord.Embed(title=f"All your tries have been exhausted. YOU HAVE LOST THE GAME",color=discord.Color.red()))
         return
        else:
         await ctx.send(embed=discord.Embed(title="That was not the number, you have 3 tries left!.",description="**GUESS THE NUMBER AGAIN, OR TAKE A HINT**",color=discord.Color.red()))
         if returnMessage(ctx,self.client) == str(number):
          await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in 2 tries",color=discord.Color.green()))
          return
         elif returnMessage(ctx,self.client) == "hint" or returnMessage(ctx,self.client) == "Hint" or returnMessage(ctx,self.client) == "h":
          if randomNumber>number:
           await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}** ",color=discord.Color.dark_purple()))
          elif randomNumber<number:
           await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** ",color=discord.Color.purple()))
         else:
          self.triesLeft=self.triesLeft-1
          if self.triesLeft==0:
           await ctx.send(embed=discord.Embed(title=f"All your tries have been exhausted. YOU HAVE LOST THE GAME",color=discord.Color.red()))
           return
          else:
           await ctx.send(embed=discord.Embed(title="That was not the number, you have 2 tries left!.",description="**GUESS THE NUMBER AGAIN, OR TAKE A HINT**",color=discord.Color.red()))
           if returnMessage(ctx,self.client) == str(number):
            await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in 3 tries",color=discord.Color.green()))
            return
           elif returnMessage(ctx,self.client) == "hint" or returnMessage(ctx,self.client) == "Hint" or returnMessage(ctx,self.client) == "h":
            if randomNumber>number:
             await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}** ",color=discord.Color.dark_purple()))
            elif randomNumber<number:
             await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** ",color=discord.Color.purple()))
           else:
            self.triesLeft=self.triesLeft-1
            if self.triesLeft==0:
             await ctx.send(embed=discord.Embed(title=f"All your tries have been exhausted. YOU HAVE LOST THE GAME",color=discord.Color.red()))
             return
            else:
             await ctx.send(embed=discord.Embed(title="That was not the number, you have 1 try left!.",description="**GUESS THE NUMBER AGAIN, OR TAKE A HINT**",color=discord.Color.red()))
             if returnMessage(ctx,self.client) == str(number):
              await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in 4 tries",color=discord.Color.green()))
              return
             elif returnMessage(ctx,self.client) == "hint" or returnMessage(ctx,self.client) == "Hint" or returnMessage(ctx,self.client) == "h":
              if randomNumber>number:
               await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}** ",color=discord.Color.dark_purple()))
              elif randomNumber<number:
               await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** ",color=discord.Color.purple()))
             else:
              self.triesLeft=self.triesLeft-1
              if self.triesLeft==0:
               await ctx.send(embed=discord.Embed(title=f"All your tries have been exhausted. YOU HAVE LOST THE GAME",color=discord.Color.red()))
               return
              else:
               await ctx.send(embed=discord.Embed(title="That was not the number, you have no tries left!.",description="**GUESS THE NUMBER AGAIN, OR TAKE A HINT**",color=discord.Color.red()))
               if returnMessage(ctx,self.client) == str(number):
                await ctx.send(embed=discord.Embed(title=f"You have correctly guessed the number in 5 tries",color=discord.Color.green()))
                return
               elif returnMessage(ctx,self.client) == "hint" or returnMessage(ctx,self.client) == "Hint" or returnMessage(ctx,self.client) == "h":
                if randomNumber>number:
                 await ctx.send(embed=discord.Embed(title=f"The number is lower than **{randomNumber}** ",color=discord.Color.dark_purple()))
                elif randomNumber<number:
                 await ctx.send(embed=discord.Embed(title=f"The number is higher than **{randomNumber}** ",color=discord.Color.purple()))
                                     

'''


           