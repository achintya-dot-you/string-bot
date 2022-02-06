from discord.ext import commands
import discord
import datetime
import myBot
def increaseCommandsUsed(userid, username):
 myBot.cursor.execute(f"INSERT INTO economy (user_id,username, balance, commands_used, fc) VALUES ({userid},'{username}',1000,1, 0) ON DUPLICATE KEY UPDATE commands_used = commands_used+1;")
 myBot.db.commit()
prefixofGuild = ""
class CommandEvents(commands.Cog):
 def __init__(self,client):

  self.client=client
 @commands.Cog.listener()
 async def on_ready(self):
  print(f'{self.client.user} has logged in!')
  await self.client.change_presence(status=discord.Status.idle, activity=discord.Game(name="==help"))
 @commands.Cog.listener()
 async def on_guild_join(self,guild):
  myBot.cursor.execute(f"CREATE TABLE a{guild.id}(user_id BIGINT PRIMARY KEY,username VARCHAR(37), messages_sent BIGINT);")
  myBot.cursor.execute(f"INSERT INTO guildIds(guildId, prefix) VALUES({guild.id},'==') ON DUPLICATE KEY UPDATE prefix=prefix;")
  myBot.db.commit()
 @commands.Cog.listener()
 async def on_message(self,message):
  if message.author.id == self.client.user.id:
    return
  myBot.cursor.execute(f"SELECT prefix FROM guildIds WHERE guildId = {message.guild.id};")
  abc = myBot.cursor.fetchone()
  prefix = abc[0]
  
  if message.content=="<@!939185469315489853>":
    ctx=message.channel
    author = message.author.id
    myBot.cursor.execute(f"SELECT prefix FROM guildIds WHERE guildId = {ctx.guild.id};")
    abc = myBot.cursor.fetchone()
    prefix = abc[0]
    await ctx.send(f'Hey <@{author}>, My prefix is `{prefix}`')
    return
  if message.content.startswith(prefixofGuild):  
    increaseCommandsUsed(message.author.id,message.author)

  myBot.cursor.execute(f"INSERT INTO a{message.guild.id} (user_id, username, messages_sent) VALUES ({message.author.id},'{message.author}',1) ON DUPLICATE KEY UPDATE messages_sent=messages_sent+1;")
  myBot.db.commit()


  #await self.client.process_commands(message)
def setup(client):
 client.add_cog(CommandEvents(client))