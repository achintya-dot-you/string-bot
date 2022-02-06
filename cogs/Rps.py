from discord.ext import commands
import discord
import myBot
import random
from discord.commands import Option,slash_command
def updateRpsWon(userid,username):
 myBot.cursor.execute(f"INSERT INTO economy(user_id,username,rps_won) VALUES ({userid},{username},1) ON DUPLICATE KEY UPDATE rps_won = rps_won + 1")
 myBot.db.commit()
randChoice = random.choice(["Rock","Paper","Scissors"])
class MyView(discord.ui.View):
 def __init__(self, ctx,client):
     super().__init__(timeout=35)
     self.ctx=ctx
     self.client=client
 @discord.ui.button(emoji = "👊",style=discord.ButtonStyle.primary)
 async def button_callback(self,button,interaction):
  if randChoice == "Rock":
   embed=discord.Embed(title="You drew the game",color=discord.Color.dark_grey())
   embed.add_field(name="Bot's Choice",value = "👊",inline=True)
   embed.add_field(name="Your Choice",value = "👊",inline=True)
   embed.set_footer(text="cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  elif randChoice == "Paper":
   embed=discord.Embed(title="You lost the game",color=discord.Color.red())
   embed.add_field(name="Bot's Choice",value = "🖐",inline=True)
   embed.add_field(name="Your Choice",value = "👊",inline=True)
   embed.set_footer(text="not cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  elif randChoice=="Scissors":
   embed=discord.Embed(title="You won the game",color=discord.Color.green())
   embed.add_field(name="Bot's Choice",value = "✌",inline=True)
   embed.add_field(name="Your Choice",value = "👊",inline=True)
   embed.set_footer(text="very cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
   updateRpsWon(self.ctx.author.id,self.ctx.author)
  else:
   await interaction.response.edit_message("**I got an error what the heck**",view=None)

 @discord.ui.button(emoji = "🖐",style=discord.ButtonStyle.primary)
 async def button_callback1(self,button,interaction):
  if randChoice == "Rock":
   embed=discord.Embed(title="You won the game",color=discord.Color.green())
   embed.add_field(name="Bot's Choice",value = "👊",inline=True)
   embed.add_field(name="Your Choice",value = "🖐",inline=True)
   embed.set_footer(text="very cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)

   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
   updateRpsWon(self.ctx.author.id,self.ctx.author)
  elif randChoice == "Paper":
   embed=discord.Embed(title="You drew the game",color=discord.Color.dark_grey())
   embed.add_field(name="Bot's Choice",value = "🖐",inline=True)
   embed.add_field(name="Your Choice",value = "🖐",inline=True)
   embed.set_footer(text="cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  elif randChoice=="Scissors":
   embed=discord.Embed(title="You lost the game",color=discord.Color.red())
   embed.add_field(name="Bot's Choice",value = "✌",inline=True)
   embed.add_field(name="Your Choice",value = "🖐",inline=True)
   embed.set_footer(text="not cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  else:
   await interaction.response.edit_message("**I got an error what the heck**",view=None)
 @discord.ui.button(emoji = "✌",style=discord.ButtonStyle.primary)
 async def button_callback2(self,button,interaction):
  if randChoice == "Rock":
   embed=discord.Embed(title="You lost the game",color=discord.Color.red())
   embed.add_field(name="Bot's Choice",value = "👊",inline=True)
   embed.add_field(name="Your Choice",value = "✌",inline=True)
   embed.set_footer(text="not cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  elif randChoice == "Paper":
   embed=discord.Embed(title="You won the game",color=discord.Color.green())
   embed.add_field(name="Bot's Choice",value = "🖐",inline=True)
   embed.add_field(name="Your Choice",value = "✌",inline=True)
   embed.set_footer(text="very cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
   updateRpsWon(self.ctx.author.id,self.ctx.author)
  elif randChoice=="Scissors":
   embed=discord.Embed(title="You drew the game",color=discord.Color.dark_grey())
   embed.add_field(name="Bot's Choice",value = "✌",inline=True)
   embed.add_field(name="Your Choice",value = "✌",inline=True)
   embed.set_footer(text="cool.",icon_url=self.client.user.display_avatar)
   await interaction.response.edit_message(embed=embed,view=None)
   myBot.increaseCommandsUsed(self.ctx.author.id,self.ctx.author)
  else:
   await interaction.response.edit_message("**I got an error what the heck**",view=None)

 async def interaction_check(self, interaction:discord.Interaction) -> bool:
    if interaction.user != self.ctx.author:
        await interaction.response.send_message("yeah good luck playing someone else's game", ephemeral=True)
        return False
    else:
        return True


class Rps(commands.Cog):
 def __init__(self,client):
     self.client=client
 @slash_command(name="rps",description="play rps with the bot")
 async def rps1(self,ctx):
  await ctx.defer()
  view = MyView(ctx,self.client)
  await ctx.respond(embed=discord.Embed(title="Pick rock, paper or scissors!",color=discord.Color.purple()),view=view)

 @commands.command(aliases=["rps"])
 async def rockpaperscissors(self,ctx):
  view=MyView(ctx,self.client)
  await ctx.send(embed=discord.Embed(title="Pick rock, paper or scissors!",color=discord.Color.purple()),view=view)
  


def setup(client):
 client.add_cog(Rps(client))