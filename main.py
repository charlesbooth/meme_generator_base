import discord
import os
import time

from dotenv import load_dotenv, find_dotenv

from meme import make_meme


intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  '''ignore message from bot'''
  if message.author == client.user:
    return

  '''check if message has $ and additional text'''
  if message.content.startswith('$') and message.attachments:
    '''split message into sections (used for top and bottom text)'''
    msg = message.content[1:].split('-')

    '''if message is empty (aside from $), end it and return message'''
    if not msg:
      await message.channel.send('Get me-a some a real-a food!!')
      return

    '''assign top text'''
    top_text = msg[0]

    '''assign bottom text, if applicable / if not, only use top'''
    if len(msg) > 1:
      bottom_text = msg[1]

    '''get url from attachment'''
    attachment_link = message.attachments[0].url

    '''delete message and send start-up feedback'''
    await message.delete()
    await message.channel.send('*Turns on stove.*')

    '''create the meme'''
    meme_link = make_meme(attachment_link,
                          top_text,
                          bottom_text)
  
    '''return link to meme'''
    await message.channel.send(meme_link)

'''start bot'''
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
