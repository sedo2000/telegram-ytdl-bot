from telegram import Update
from telegram.ext import ContextTypes
from .downloader import download_video
from .admin import is_admin

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أرسل رابط يوتيوب واختر:\n/mp3\n/mp4"
    )

async def mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.reply_to_message.text
    path = download_video(url, "bestaudio/best")
    await update.message.reply_audio(audio=open(path, "rb"))

async def mp4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.reply_to_message.text
    path = download_video(url, "bestvideo+bestaudio/best")
    await update.message.reply_video(video=open(path, "rb"))
