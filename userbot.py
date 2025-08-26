import asyncio
from datetime import datetime
from telethon import TelegramClient, events
import os

# 🔑 API ma'lumotlarini Environment Variables orqali olish
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = "userbot_session"

# Telegram client
client = TelegramClient(SESSION, API_ID, API_HASH)

# 🕒 Soat style funksiya
def styled_clock():
    now = datetime.now().strftime("%H:%M:%S")
    style = f"⏰ [{now}] ⏰"
    return style

# 🤖 Faqat "licka" ga javob beradigan auto-reply
@client.on(events.NewMessage(pattern="licka", incoming=True))
async def auto_reply(event):
    reply_text = f"Salom 😊\nMana hozirgi vaqt: {styled_clock()}"
    await event.reply(reply_text)

# 🔄 Userbot ishga tushishi
async def main():
    print("✅ Userbot ishlayapti...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
