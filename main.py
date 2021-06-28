import discord
import os
import asyncio
import random
from discord.ext  import commands
bot = commands.Bot(command_prefix = '--')
bot.sniped_messages = {}

@bot.event 
async def on_ready():
  print("bot is ready")

@bot.event
async def on_message_delete(message):
  bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@bot.command()
async def snipe(ctx):
  try:
   contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]

  except:
    await ctx.channel.send("Couldn't find a message to snipe")
    return 
  embed = discord.Embed(description=contents, color=discord.Color.blurple(), timestamp=time)
  embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
  embed.set_footer(text=f"Deleted in : #{channel_name}")

  await ctx.channel.send(embed=embed)

@bot.command()
async def ping(ctx):
  await ctx.send('pong!')

@bot.command()
async def hi(ctx):
  await ctx.send('aren\'t you fucking lonely?')

@bot.command()
async def coinflip(ctx):

  faces = ['heads', 'tails']

  random_face = random.choice(faces)

  await ctx.send(random_face) 

@bot.command()
async def sup(ctx):
  up = ["I'm doing great!", "meh", "I'm fine, I think", " could be way better", "not good", "I wanna die badly", "fuck off please", "fuck off", "lonely as fuck"]
  
  random_up = random.choice(up)

  await ctx.send(random_up)

#countdown from rex-rim
@bot.command()
async def countdown(ctx, seconds=None , type=None, *, timername=None):
  if not timername:
    await ctx.send("`countdown <time in seconds> <timer name>`") 
    raise BaseException
  if not seconds:
    await ctx.send("`countdown <time in seconds> <timer name>`") 
    raise BaseException
  secondint = int(seconds)
  if type == "m":
      secondint = secondint * 60
  elif type == "h":
     secondint = secondint * 3600
  elif type == "s":
     secondint = secondint * 1
  try:
    if secondint <= 0:
      await ctx.send("`Error number`")
      raise BaseException
    message = await ctx.send(f"`{timername}: {seconds}`")
    while True:
      secondint -= 1
      if secondint == 0:
        await message.edit(content=f"`{timername} ended`{ctx.message.author.mention}")
        break
      await message.edit(content=f"`{timername} {secondint}`")
      await asyncio.sleep(1)
  except ValueError:
    await ctx.send("`Error number`")


Token = os.environ.get('DISCB_TOKEN')
bot.run(Token)
