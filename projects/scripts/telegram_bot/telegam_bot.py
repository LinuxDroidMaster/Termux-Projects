import os
from telegram.ext import (Updater, CommandHandler)
import yt_dlp

def start(update, context):
    # When /start is received send "Welcome" text.
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome")


def download_youtube_video(update, context):
    # Extract the URL from the command (e.g. /youtube URL)
    if context.args:
        url = context.args[0]
        
        # Define options for yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,  # Ensure that only a single video is downloaded
        }
        
        try:
            # Download video using yt-dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                video_title = info_dict.get('title', 'video')

            # Notify the user that the download was successful
            context.bot.send_message(chat_id=update.message.chat_id, text=f"Video '{video_title}' has been downloaded successfully!")
        
        except Exception as e:
            # Notify the user in case of an error
            context.bot.send_message(chat_id=update.message.chat_id, text=f"An error occurred: {str(e)}")
    else:
        # If no URL is provided, inform the user
        context.bot.send_message(chat_id=update.message.chat_id, text="Please provide a valid YouTube URL. Usage: /youtube <URL>")


def main():
    TOKEN = "TOKEN_VALUE_FROM_BOTFATHER"

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Event handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('youtube', download_youtube_video))

    # Start bot
    updater.start_polling()

    # Bot listening.
    updater.idle()


if __name__ == '__main__':
    main()