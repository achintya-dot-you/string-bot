from discord.ext import commands
import discord
import myBot
import random
from discord.commands import Option,slash_command
dictabc = {1:"1️⃣",2:"2️⃣",3:"3️⃣",4:"4️⃣",6:"6️⃣"}

def updateHighestScore(userid,username,scoreRn):
  myBot.cursor.execute(f"INSERT INTO economy (user_id, username, balance, commands_used, highest_score) VALUES ({userid},'{username}', 1000, 0,{scoreRn}) ON DUPLICATE KEY UPDATE highest_score = highest_score;")
  myBot.db.commit()
  myBot.cursor.execute(f"SELECT highest_score FROM economy WHERE user_id={userid};")
  highestScore = myBot.cursor.fetchone()
  if highestScore[0] < scoreRn:
    myBot.cursor.execute(f"UPDATE economy SET highest_score = {scoreRn} WHERE user_id={userid};")
    myBot.db.commit()
  else:
    pass
def embedreturn(botChoice:int,userChoice:int, message:str,color : discord.Color):                      
  embed = discord.Embed(color=color)
  embed.add_field(name="Bot's choice: ",value=f"{dictabc[botChoice]}",inline = True)
  embed.add_field(name="Your choice: ",value=f"{dictabc[userChoice]}", inline = True)
  embed.add_field(name="Result: ",value = message, inline=False)
  return embed
def embedreturn2(botChoice:int,userChoice:int, message:str,color : discord.Color):                      
  embed = discord.Embed(color=color)
  embed.add_field(name="Bot's choice: ",value=f"{dictabc[botChoice]}",inline = True)
  embed.add_field(name="Your choice: ",value=f"{dictabc[userChoice]}", inline = True)
  

  embed.add_field(name="Result: ",value = message, inline=False)
  return embed
def embedreturn1(botChoice:int,userChoice:int, message:str,color : discord.Color):                      
  embed = discord.Embed(color=color)
  embed.add_field(name="Your choice: ",value=f"{dictabc[userChoice]}", inline = True)
  embed.add_field(name="Bot's choice: ",value=f"{dictabc[botChoice]}",inline = True)

  embed.add_field(name="Result: ",value = message, inline=False)
  return embed
def makeEmbed(color:discord.Color=discord.Color.dark_grey(),title:str=None,description:str=None):

  embed = discord.Embed(title=title,description=description,color=color)
  return embed

def newNum():
  number=random.choice([1,2,3,4,6])
  return number
def botGeneration():
  botNumber= random.choice([1,2,3,4,6])
  return dictabc[botNumber]

class TransitionView(discord.ui.View):
  def __init__(self, ctx, nextview:discord.ui.View):
      super().__init__(timeout=35)
      self.ctx=ctx
      
      self.nextView = nextview
  
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji = "➡️")
  async def button_callback(self,button,interaction):
    await interaction.response.edit_message(embed = discord.Embed(title="Next innings is now starting.....", color = discord.Color.purple()),view=self.nextView)

class BattingSecond(discord.ui.View):
  def __init__(self,ctx,scoreToBeat:int):
      super().__init__(timeout=35)
      self.ctx=ctx
      self.score = 0
      self.rn = newNum()
      self.scoreToBeat = scoreToBeat+1
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="1️⃣")
  async def button_callback(self,button, interaction):
    if self.rn== 1:
      embed=embedreturn(self.rn,1,f"Oopsie, game over. Your were able to score **{self.score}** \n **YOU WERE {(self.scoreToBeat-1)-self.score} away from winning.**", discord.Color.red())
      embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
      embed.add_field(name="Your score",value=f"{self.score}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)

    else:

      self.score+=1
      if self.score >= self.scoreToBeat:
        embed=embedreturn(self.rn,1,f"Congratulations, you have won the game and defeated the bot. ggs", discord.Color.green())
        embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
        embed.add_field(name="Your score",value=f"{self.score}",inline=True)

        await interaction.response.edit_message(embed=embed, view = None)
        updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      else:
        await interaction.response.edit_message(embed=embedreturn(self.rn,1,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
        self.rn=newNum()

  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="2️⃣")
  async def button_callback2(self,button, interaction):
    if self.rn== 2:
      embed=embedreturn(self.rn,2,f"Oopsie, game over. Your were able to score **{self.score}** \n **YOU WERE {(self.scoreToBeat-1)-self.score} away from winning.**", discord.Color.red())
      embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
      embed.add_field(name="Your score",value=f"{self.score}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      
    else:

      self.score+=2
      if self.score >= self.scoreToBeat:
        embed=embedreturn(self.rn,2,f"Congratulations, you have won the game and defeated the bot. \n **ggs**", discord.Color.green())
        embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
        embed.add_field(name="Your score",value=f"{self.score}",inline=True)

        await interaction.response.edit_message(embed=embed, view = None)
        updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      else:
        await interaction.response.edit_message(embed=embedreturn(self.rn,2,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
        self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="3️⃣")
  async def button_callback3(self,button, interaction):
    if self.rn== 3:
      embed=embedreturn(self.rn,3,f"Oopsie, game over. Your were able to score **{self.score}** \n **YOU WERE {(self.scoreToBeat-1)-self.score} away from winning.**", discord.Color.red())
      embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
      embed.add_field(name="Your score",value=f"{self.score}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      
    else:

      self.score+=3
      if self.score >= self.scoreToBeat:
        embed=embedreturn(self.rn,3,f"Congratulations, you have won the game and defeated the bot. \n **ggs!**", discord.Color.green())
        embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
        embed.add_field(name="Your score",value=f"{self.score}",inline=True)

        await interaction.response.edit_message(embed=embed, view = None)
        updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      else:
        await interaction.response.edit_message(embed=embedreturn(self.rn,3,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
        self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="4️⃣")
  async def button_callback4(self,button, interaction):
    if self.rn== 4:
      embed=embedreturn(self.rn,4,f"Oopsie, game over. Your were able to score **{self.score}** \n **YOU WERE {(self.scoreToBeat-1)-self.score} away from winning.**", discord.Color.red())
      embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
      embed.add_field(name="Your score",value=f"{self.score}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
    else:

      self.score+=4
      if self.score >= self.scoreToBeat:
        embed=embedreturn(self.rn,4,f"Congratulations, you have won the game and defeated the bot. \n **ggs!**", discord.Color.green())
        embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
        embed.add_field(name="Your score",value=f"{self.score}",inline=True)

        await interaction.response.edit_message(embed=embed, view = None)
        updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      else:
        await interaction.response.edit_message(embed=embedreturn(self.rn,4,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
        self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="6️⃣")
  async def button_callback6(self,button, interaction):
    if self.rn== 6:
      embed=embedreturn(self.rn,6,f"Oopsie, game over. Your were able to score **{self.score}** \n **YOU WERE {(self.scoreToBeat-1)-self.score} away from winning.**", discord.Color.red())
      embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
      embed.add_field(name="Your score",value=f"{self.score}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
    else:

      self.score+=6
      if self.score >= self.scoreToBeat:
        embed=embedreturn(self.rn,6,f"Congratulations, you have won the game and defeated the bot. \n **ggs!**", discord.Color.green())
        embed.add_field(name="Bot's score",value=f"{self.scoreToBeat-1}",inline=True)
        embed.add_field(name="Your score",value=f"{self.score}",inline=True)

        await interaction.response.edit_message(embed=embed, view = None)
        updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      else:
        await interaction.response.edit_message(embed=embedreturn(self.rn,6,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
        self.rn=newNum()



  async def interaction_check(self, interaction:discord.Interaction) -> bool:
    if interaction.user != self.ctx.author:
        await interaction.response.send_message("yeah good luck playing someone else's game", ephemeral=True)
        return False
    else:
        return True

class BowlingSecond(discord.ui.View):
  def __init__(self,ctx, personScore : int):
    super().__init__(timeout=35)
    self.ctx=ctx
    self.rn = newNum()
    self.score = 0
    self.personScore = personScore
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="1️⃣")
  async def button_callback(self,button,interaction):
    if self.rn == 1:

      embed=embedreturn(self.rn,1,f"Congratulations, the bot is out! \n **YOU WON BY {(self.personScore)-self.score} runs.**", discord.Color.green())
      embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
      embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)

    elif self.rn != 1:
      self.score+=self.rn
      if self.score>= self.personScore:
        embed=embedreturn(self.rn,1,f"Oh no, the bot **beat your score.** You have lost the game. **Better luck next time :(**", discord.Color.red())
        embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
        embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

        await interaction.response.edit_message(embed=embed,view=None)
      else:
        await interaction.response.edit_message(embed=embedreturn1(self.rn,1,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
        self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="2️⃣")
  async def button_callback1(self,button,interaction):
    if self.rn == 2:

      embed=embedreturn(self.rn,2,f"Congratulations, the bot is out! \n **YOU WON BY {(self.personScore)-self.score} runs.**", discord.Color.green())
      embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
      embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)

    elif self.rn != 2:
      self.score+=self.rn
      if self.score>= self.personScore:
        embed=embedreturn(self.rn,2,f"Oh no, the bot **beat your score.** You have lost the game. **Better luck next time :(**", discord.Color.red())
        embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
        embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

        await interaction.response.edit_message(embed=embed,view=None)
      else:
        await interaction.response.edit_message(embed=embedreturn1(self.rn,2,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
        self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="3️⃣")
  async def button_callback2(self,button,interaction):
    if self.rn == 3:

      embed=embedreturn(self.rn,3,f"Congratulations, the bot is out! \n **YOU WON BY {(self.personScore)-self.score} runs.**", discord.Color.green())
      embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
      embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)

    elif self.rn != 3:
      self.score+=self.rn
      if self.score>= self.personScore:
        embed=embedreturn(self.rn,3,f"Oh no, the bot **beat your score.** You have lost the game. **Better luck next time :(**", discord.Color.red())
        embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
        embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

        await interaction.response.edit_message(embed=embed,view=None)
      else:
        await interaction.response.edit_message(embed=embedreturn1(self.rn,3,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
        self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="4️⃣")
  async def button_callback3(self,button,interaction):
    if self.rn == 4:

      embed=embedreturn(self.rn,4,f"Congratulations, the bot is out! \n **YOU WON BY {(self.personScore)-self.score} runs.**", discord.Color.green())
      embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
      embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)

    elif self.rn != 4:
      self.score+=self.rn
      if self.score>= self.personScore:
        embed=embedreturn(self.rn,4,f"Oh no, the bot **beat your score.** You have lost the game. **Better luck next time :(**", discord.Color.red())
        embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
        embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

        await interaction.response.edit_message(embed=embed,view=None)
      else:
        await interaction.response.edit_message(embed=embedreturn1(self.rn,4,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
        self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="6️⃣")
  async def button_callback4(self,button,interaction):
    if self.rn == 6:

      embed=embedreturn(self.rn,6,f"Congratulations, the bot is out! \n **YOU WON BY {(self.personScore)-self.score} runs.**", discord.Color.green())
      embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
      embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

      await interaction.response.edit_message(embed=embed,view=None)

    elif self.rn != 6:
      self.score+=self.rn
      if self.score>= self.personScore:
        embed=embedreturn(self.rn,6,f"Oh no, the bot **beat your score.** You have lost the game. **Better luck next time :(**", discord.Color.red())
        embed.add_field(name="Bot's score",value=f"{self.score}",inline=True)
        embed.add_field(name="Your score",value=f"{self.personScore}",inline=True)

        await interaction.response.edit_message(embed=embed,view=None)
      else:
        await interaction.response.edit_message(embed=embedreturn1(self.rn,6,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
        self.rn=newNum()
  


class BowlingFirst(discord.ui.View):
  def __init__(self, ctx):
      super().__init__(timeout=35)
      self.ctx=ctx
      self.rn = newNum()
      self.score = 0
  
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="1️⃣")
  async def button_callback(self,button,interaction):
    if self.rn == 1:
      await interaction.response.edit_message(embed=embedreturn1(self.rn,1,f"Congratulations, the bot is **OUT**. \n **Its final score was {self.score}**. Now you have to chase the bot's score. \n **Continue?**", discord.Color.green()), view=TransitionView(self.ctx,BattingSecond(self.ctx,self.score)))
    elif self.rn != 1:
      self.score+=self.rn
      await interaction.response.edit_message(embed=embedreturn1(self.rn,1,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
      self.rn=newNum()
      
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="2️⃣")
  async def button_callback1(self,button,interaction):
    if self.rn == 2:
      await interaction.response.edit_message(embed=embedreturn1(self.rn,2,f"Congratulations, the bot is **OUT**. \n **Its final score was {self.score}**. Now you have to chase the bot's score. \n **Continue?**", discord.Color.green()), view=TransitionView(self.ctx,BattingSecond(self.ctx,self.score))) 
    elif self.rn != 2:
      self.score+=self.rn
      await interaction.response.edit_message(embed=embedreturn1(self.rn,2,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
      self.rn=newNum()
      
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="3️⃣")
  async def button_callback2(self,button,interaction):
    if self.rn == 3:
      await interaction.response.edit_message(embed=embedreturn1(self.rn,3,f"Congratulations, the bot is **OUT**. \n **Its final score was {self.score}**. Now you have to chase the bot's score. \n **Continue?**", discord.Color.green()), view=TransitionView(self.ctx,BattingSecond(self.ctx,self.score)))

    elif self.rn != 3:
      self.score+=self.rn
      await interaction.response.edit_message(embed=embedreturn1(self.rn,3,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
      self.rn=newNum()
      
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="4️⃣")
  async def button_callback3(self,button,interaction):
    if self.rn == 4:
      await interaction.response.edit_message(embed=embedreturn1(self.rn,4,f"Congratulations, the bot is **OUT**. \n **Its final score was {self.score}**. Now you have to chase the bot's score. \n **Continue?**", discord.Color.green()), view=TransitionView(self.ctx, BattingSecond(self.ctx,self.score)))
    elif self.rn != 4:
      self.score+=self.rn
      await interaction.response.edit_message(embed=embedreturn1(self.rn,4,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
      self.rn=newNum()
      
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="6️⃣")
  async def button_callback4(self,button,interaction):
    if self.rn == 6:
      await interaction.response.edit_message(embed=embedreturn1(self.rn,6,f"Congratulations, the bot is **OUT**. \n **Its final score was {self.score}**. Now you have to chase the bot's score. \n **Continue?**", discord.Color.green()), view=TransitionView(self.ctx,BattingSecond(self.ctx,self.score)))
    elif self.rn != 6:
      self.score+=self.rn
      await interaction.response.edit_message(embed=embedreturn1(self.rn,6,f"Not out **:(** the bot has scored **{self.score}** till now", discord.Color.dark_grey()))
      self.rn=newNum()
      
          



#-----------------------------------------------------------------------------
class BattingFirst(discord.ui.View):
  def __init__(self,ctx,):
        super().__init__(timeout=300)
        self.rn = newNum()
        self.score = 0
        self.ctx=ctx
        


  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="1️⃣")
  async def button_callback(self,button, interaction):
    if self.rn== 1:
      await interaction.response.edit_message(embed=embedreturn(self.rn,1,f"Oopsie, game over. Your final score was **{self.score}**", discord.Color.red()),view=TransitionView(self.ctx,BowlingSecond(self.ctx,self.score)))
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)

    else:

      self.score+=1
    
      await interaction.response.edit_message(embed=embedreturn(self.rn,1,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
      self.rn=newNum()

  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="2️⃣")
  async def button_callback2(self,button, interaction):
    if self.rn== 2:
      await interaction.response.edit_message(embed=embedreturn(self.rn,2,f"Oopsie, game over. Your final score was **{self.score}**", discord.Color.red()),view=TransitionView(self.ctx,BowlingSecond(self.ctx,self.score)))
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      
    else:
      self.score+=2
      
      await interaction.response.edit_message(embed=embedreturn(self.rn,2,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
      self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="3️⃣")
  async def button_callback3(self,button, interaction):
    if self.rn== 3:
      await interaction.response.edit_message(embed=embedreturn(self.rn,3,f"Oopsie, game over. Your final score was **{self.score}**", discord.Color.red()),view=TransitionView(self.ctx,BowlingSecond(self.ctx,self.score)))
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
      
    else:
      self.score+=3
      
      await interaction.response.edit_message(embed=embedreturn(self.rn,3,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
      self.rn=newNum()
  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="4️⃣")
  async def button_callback4(self,button, interaction):
    if self.rn== 4:
      await interaction.response.edit_message(embed=embedreturn(self.rn,4,f"Oopsie, game over. Your final score was **{self.score}**", discord.Color.red()),view=TransitionView(self.ctx,BowlingSecond(self.ctx,self.score)))
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
    else:
      self.score+=4
      
      await interaction.response.edit_message(embed=embedreturn(self.rn,4,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
      self.rn=newNum()

  @discord.ui.button(style=discord.ButtonStyle.primary,emoji="6️⃣")
  async def button_callback6(self,button, interaction):
    if self.rn== 6:
      await interaction.response.edit_message(embed=embedreturn(self.rn,6,f"Oopsie, game over. Your final score was **{self.score}**", discord.Color.red()),view=TransitionView(self.ctx,BowlingSecond(self.ctx,self.score)))
      updateHighestScore(self.ctx.author.id,self.ctx.author,self.score)
    else:
      self.score+=6
      
      await interaction.response.edit_message(embed=embedreturn(self.rn,6,f"Congratulations, you have scored **{self.score}** till now", discord.Color.green()))
      self.rn=newNum()



  async def interaction_check(self, interaction:discord.Interaction) -> bool:
    if interaction.user != self.ctx.author:
        await interaction.response.send_message("yeah good luck playing someone else's game", ephemeral=True)
        return False
    else:
        return True

class MyView2(discord.ui.View):
  def __init__(self,ctx):
        super().__init__(timeout=60)
        self.ctx=ctx

  
  @discord.ui.button(label="Batting",custom_id="batButton",style=discord.ButtonStyle.primary)
  async def button_callback(self,button,interaction):
    embed = discord.Embed(description = "The game of cricket is now starting. Below, you see 5 Buttons, pick one, if your choice and the bot's choice is the same, you get eliminated, if not, you continue playing and your number chosen adds up to your score. \n **YOU ARE BATTING FIRST**", color = discord.Color.purple())
    await interaction.response.edit_message(embed=embed,view=BattingFirst(self.ctx))
  @discord.ui.button(label="Bowling",custom_id="bowlButton",style=discord.ButtonStyle.primary)
  async def button_callback1(self,button,interaction):
    embed = discord.Embed(description = "Below, you see 5 Buttons, pick one, if your choice and the bot's choice is the same, you get eliminated,the bot gets eliminated. if not, you continue playing and your number chosen adds up to your score. \n **YOU ARE BOWLING FIRST**", color = discord.Color.purple())
    await interaction.response.edit_message(embed=embed,view=BowlingFirst(self.ctx))





class MyView1(discord.ui.View):
  def __init__(self,ctx):
        super().__init__(timeout=30)
        self.ht = "h"
        self.personChoice=True
        self.ctx=ctx
  
  @discord.ui.button(label="Heads",custom_id="headsButton",style= discord.ButtonStyle.primary)
  async def button_callback(self,button,interaction):
    if self.ht == "h":
      embed=discord.Embed(title="You won the toss, pick batting or bowling. ",color=discord.Color.green())
      await interaction.response.edit_message(content="",view=MyView2(self.ctx),embed = embed)
    elif self.ht=="t":
      await interaction.edit_original_message(embed=makeEmbed(discord.Color.red(),"You have lost the toss! I chose **bowling**!"))
  @discord.ui.button(label="Tails", custom_id = "tailsButton",style=discord.ButtonStyle.primary)
  async def button_callback1(self,button,interaction):
    if self.ht == "h":
      await interaction.response.edit_message(embed=makeEmbed(discord.Color.red(),"You have lost the toss! I chose **bowling**!"))
     

      
    elif self.ht=="t":
      embed=discord.Embed(title="You won the toss, pick batting or bowling. ",color=discord.Color.green())
      await interaction.response.edit_message(view=MyView2(self.ctx),embed=embed) 



class Cricket(commands.Cog):
  def __init__(self,client):
    self.client=client
  @slash_command(name="cricket", description="Play cricket with the bot or another member")
  async def cricket(ctx,member:Option(discord.Member,"Member to play cricket with", required=False, default=None)):
    await ctx.defer()
    embed = discord.Embed(description = "The game of cricket is now starting. Below, you see 5 Buttons, pick one, if your choice and the bot's choice is the same, you get eliminated, if not, you continue playing and your number chosen adds up to your score", color = discord.Color.purple())

    view=MyView1(ctx)
    #res = await view.wait()
    
    # if res:
    #   for i in view.children:
    #       i.disabled=True
    message =  await ctx.respond("Pick heads or tails",view=view)
    myBot.increaseCommandsUsed(ctx.author.id,ctx.author)


  @commands.command()
  async def cricket(self,ctx):
    embed= discord.Embed(description="The game of cricket with the bot is now starting. \n\n **PICK HEADS OR TAILS TO START THE GAME**", color = discord.Color.purple() )
    embed.set_footer(text="you'll probably suck at cricket heh")

    view= MyView1(ctx)
    await ctx.send(embed=embed,view=view)
  





def setup(client):
  client.add_cog(Cricket(client))

