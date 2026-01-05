import os
import asyncio
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler
from bot.handlers import start, mp3, mp4

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()
# بناء التطبيق مرة واحدة لزيادة السرعة
application = Application.builder().token(BOT_TOKEN).build()

# إضافة الأوامر
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("mp3", mp3))
application.add_handler(CommandHandler("mp4", mp4))

@app.post("/api")
async def webhook(req: Request):
    if application.running:
        data = await req.json()
        update = Update.de_json(data, application.bot)
        await application.process_update(update)
    else:
        # تشغيل التطبيق في حالة الـ Serverless
        await application.initialize()
        data = await req.json()
        update = Update.de_json(data, application.bot)
        await application.process_update(update)
    return {"ok": True}

@app.get("/")
async def index():
    return {"status": "Bot is running"}
