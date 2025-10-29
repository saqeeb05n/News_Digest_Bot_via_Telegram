import asyncio
import os
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

async def send_message_async(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(
        chat_id=int(TELEGRAM_CHAT_ID),
        text=message,
        disable_web_page_preview=True,
        parse_mode="Markdown"
    )

def send_to_telegram(message):
    asyncio.run(send_message_async(message))
