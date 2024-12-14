# assistant_bot.py

import os
import asyncio
from telethon import TelegramClient
from yt_dlp import YoutubeDL
from pydub import AudioSegment
from pydub.playback import play
from config import API_ID, API_HASH, PHONE_NUMBER

# Assistant Telegram API details
client = TelegramClient('assistant_session', API_ID, API_HASH)

async def login():
    await client.start(PHONE_NUMBER)  # Assistant account login

async def play_song_in_voice_chat(song_name, group_link):
    # Search and download song using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f"ytsearch:{song_name}", download=True)
        song_url = info_dict['entries'][0]['url']
        song_title = info_dict['entries'][0]['title']

    # Convert downloaded song to mp3
    song_path = f"downloads/{song_title}.mp3"
    
    # Play the song (using pydub for now, for real deployment you would stream it to voice chat)
    audio = AudioSegment.from_mp3(song_path)
    play(audio)
    
    # Cleanup after playing
    os.remove(song_path)  # This will delete the downloaded song file

    # Join voice chat
    group = await client.get_entity(group_link)
    await client.send_message(group, "Joining voice chat...")
    
    # Actual voice chat streaming to be added here. In this basic setup, we're playing audio locally.
    print("Playing song:", song_title)

async def main():
    await login()  # Login to Assistant account
    group_link = "https://t.me/your_group_link"  # Provide the group link where you want to join
    song_name = "Never Gonna Give You Up"  # Example song
    await play_song_in_voice_chat(song_name, group_link)

if __name__ == "__main__":
    asyncio.run(main())
