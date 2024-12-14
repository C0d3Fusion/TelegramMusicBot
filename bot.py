# bot.py

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from assistant_bot import play_song_in_voice_chat  # Import function from assistant_bot.py

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Command to play song
def play(update: Update, context: CallbackContext):
    song_name = ' '.join(context.args)
    if not song_name:
        update.message.reply_text("Please provide a song name after /play command.")
        return

    group_link = "https://t.me/thajxj28"  # Replace with your group link
    play_song_in_voice_chat(song_name, group_link)  # Call assistant bot to play song
    update.message.reply_text(f"Playing song: {song_name}")

def main():
    # Telegram Bot API key
    updater = Updater("7204900838:AAER1etGVlMYdPAxz--xQGOnjhu2b6RVKko", use_context=True)
    dp = updater.dispatcher

    # Command Handlers
    dp.add_handler(CommandHandler("play", play))  # Handle /play command

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
