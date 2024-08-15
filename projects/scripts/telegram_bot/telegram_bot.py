import os
from telegram.ext import Application, CommandHandler
import yt_dlp

# Define the /start command handler
async def start(update, context):
    await update.message.reply_text("Welcome! 🎉")

# Define the /youtube command handler to handle the video download process
async def download_youtube_video(update, context):
    # Send initial processing message
    await update.message.reply_text("📥 Message received, processing...")

    # Extract the URL from the command (e.g. /youtube URL)
    if len(context.args) > 0:
        url = context.args[0]
        
        # Define options for yt-dlp to download the best available quality
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,  # Ensure that only a single video is processed
        }
        
        try:
            # Download the video using yt-dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                video_title = info_dict.get('title', 'video')
                file_path = ydl.prepare_filename(info_dict)  # Get the downloaded file path

            # Notify the user that the download was successful
            await update.message.reply_text(f"✅ Video '{video_title}' has been downloaded successfully!")

            # Send the downloaded video file back to the user
            with open(file_path, 'rb') as video_file:
                await update.message.reply_document(video_file)
            
            # Optionally, delete the file after sending it
            os.remove(file_path)

        except Exception as e:
            # Notify the user in case of an error
            await update.message.reply_text(f"⚠️ An error occurred: {str(e)}")
    else:
        # If no URL is provided, inform the user
        await update.message.reply_text("🔗 Please provide a valid YouTube URL. Usage: /youtube <URL>")

def main():
    TOKEN = "TOKEN_VALUE_FROM_BOTFATHER"  # Replace with your actual token

    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('youtube', download_youtube_video))

    # Run the bot using polling (this blocks until the bot is stopped)
    application.run_polling()

if __name__ == '__main__':
    main()
