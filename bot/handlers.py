from telegram import Update
from telegram.ext import ContextTypes
from .downloader import download_video
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل رابط فيديو يوتيوب أولاً، ثم اضغط على:\n/mp3 - للصوت\n/mp4 - للفيديو")

async def mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # جلب النص من الرسالة الحالية أو من الرد (Reply)
    message = update.message.reply_to_message if update.message.reply_to_message else update.message
    url = message.text
    
    status = await update.message.reply_text("جاري معالجة الصوت... ⏳")
    try:
        [span_1](start_span)path = download_video(url, "bestaudio/best")[span_1](end_span)
        with open(path, "rb") as f:
            await update.message.reply_audio(audio=f)
        os.remove(path) # حذف الملف بعد الإرسال
        await status.delete()
    except Exception as e:
        await update.message.reply_text(f"خطأ: {str(e)}")

async def mp4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.reply_to_message if update.message.reply_to_message else update.message
    url = message.text
    
    status = await update.message.reply_text("جاري تحميل الفيديو... ⏳")
    try:
        [span_2](start_span)path = download_video(url, "bestvideo+bestaudio/best")[span_2](end_span)
        with open(path, "rb") as f:
            await update.message.reply_video(video=f)
        os.remove(path)
        await status.delete()
    except Exception as e:
        await update.message.reply_text(f"خطأ: {str(e)}")
