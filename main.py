import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import discord
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE yippie
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# STEP 1: BOT SETUP
intents = Intents.default()
intents.message_content = True
intents.voice_states = True
client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty)')
        return

    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')

    if user_message.startswith('!join'):
        # Join the voice channel
        if message.author.voice:
            voice_channel = message.author.voice.channel
            await voice_channel.connect()
            await message.channel.send(f'Joined {voice_channel}')
        else:
            await message.channel.send('You are not in a voice channel!')

    elif user_message.startswith('!play'):
        # Play music from a URL
        if message.guild.voice_client is not None:
            url = user_message.split(' ')[1]  # Get the URL after the command
            voice_client = message.guild.voice_client

            FFMPEG_OPTIONS = {
                'options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            }
            try:
                voice_client.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS))
                await message.channel.send(f'Now playing: {url}')
            except Exception as e:
                await message.channel.send('Error playing the audio. Please check the URL or format.')
                print(f'Error playing audio: {e}')
        else:
            await message.channel.send('I am not connected to a voice channel!')

    elif user_message.startswith('!leave'):
        # Leave the voice channel
        if message.guild.voice_client is not None:
            await message.guild.voice_client.disconnect()
            await message.channel.send('Disconnected from the voice channel.')
        else:
            await message.channel.send('I am not in a voice channel!')

    await send_message(message, user_message)

# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()
