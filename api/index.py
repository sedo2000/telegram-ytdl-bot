import os
import asyncio
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler
from bot.handlers import start, mp3, mp4

BOT_TOKEN = os.getenv("BOT_TOKEN")
YOUTUBE_KEY = os.getenv("YOUTUBE_API_KEY") # استدعاء مفتاح يوتيوب هنا عند الحاجة

app = FastAPI()
application = Application.builder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("mp3", mp3))
application.add_handler(CommandHandler("mp4", mp4))

@app.post("/api")
async def webhook(req: Request):
    data = await req.json()
    await application.initialize()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"ok": True}
