import discord
import os

from dotenv import load_dotenv, find_dotenv

from meme import make_meme

from collections import deque


intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True

client = discord.Client(intents=intents)

meme_queue = deque([])

@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #'''ignore message from bot'''
  if message.author == client.user:
    return

  #'''check if message has !mc, attachments, and text'''
  if message.content.lower().startswith('$mc'):
    #'''check if message has attachments / if not, delete and return'''
    if not message.attachments:
       await message.delete()
       await message.channel.send('**Your-a message has-a no attachments, so add-a some attachments. Capeesh??**')
       return
    
    #'''split message and store / delete message'''
    msg = message.content[3:].split('~', 1)
    await message.delete()

    #'''check if message has proper text / if not, return'''
    if not msg[0]:
      await message.channel.send('**Get me-a some a real-a food!! Add-a some-a text!**')
      return
    
    meme_info = tuple()
    
    #'''get message attachment url'''
    attachment_link = message.attachments[0].url
    meme_info += (attachment_link,)

    #'''assign top text'''
    top_text = msg[0].strip()
    meme_info += (top_text,)

    #'''assign bottom text, if applicable / if not, only use top'''
    if len(msg) > 1:
      bottom_text = msg[1].strip()
      meme_info += (bottom_text,)

    #'''store info in queue'''
    meme_queue.append(meme_info)
    await message.channel.send('***Turns on stove.***')

    while meme_queue:
      current_meme = meme_queue.popleft()
      meme_link = make_meme(*current_meme)
      message.delete()
      await message.channel.send(meme_link)
      if not meme_queue:
         break


#'''start bot'''
try:
    load_dotenv(find_dotenv())
    code = os.environ.get('CODE')
    client.run(code)
except(TypeError):
    print('',
          'Failure to start.',
          'Make sure project directory contains .env file.',
          sep = '\n')
except(discord.errors.LoginFailure):
    print('',
          'Invalid token was given.',
          'Make sure token is entered correctly/not expired.',
          sep = '\n')
