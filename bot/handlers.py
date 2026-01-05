from telegram import Update
from telegram.ext import ContextTypes
from .downloader import download_video
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك! أرسل رابط الفيديو كـ 'رد' (Reply) ثم اختر:\n/mp3 - لتحميل صوت\n/mp4 - لتحميل فيديو"
    )

async def mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return await update.message.reply_text("يرجى عمل Reply على رابط الفيديو.")
    
    url = update.message.reply_to_message.text
    status_msg = await update.message.reply_text("جاري تحويل ومعالجة الصوت... ⏳")
    
    try:
        path = download_video(url, "bestaudio/best")
        with open(path, "rb") as audio:
            await update.message.reply_audio(audio=audio, title="Downloaded Audio")
        os.remove(path) # حذف الملف لتوفير مساحة Vercel
        await status_msg.delete()
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {str(e)}")

async def mp4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return await update.message.reply_text("يرجى عمل Reply على رابط الفيديو.")
    
    url = update.message.reply_to_message.text
    status_msg = await update.message.reply_text("جاري تحميل الفيديو... ⏳")
    
    try:
        path = download_video(url, "bestvideo+bestaudio/best")
        with open(path, "rb") as video:
            await update.message.reply_video(video=video, caption="تم التحميل بواسطة بوتك")
        os.remove(path)
        await status_msg.delete()
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {str(e)}")
