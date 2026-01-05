import os
from fastapi import FastAPI, Request
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)
from bot.handlers import start, mp3, mp4

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()
application = Application.builder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("mp3", mp3))
application.add_handler(CommandHandler("mp4", mp4))

@app.post("/api")
async def webhook(req: Request):
    data = await req.json()
    await application.initialize()
    await application.process_update(
        application.bot.de_json(data)
    )
    return {"ok": True}
