import asyncio
from datetime import datetime
from telethon import TelegramClient, events

API_ID = 21716532
API_HASH = "4a9ea732220e7d827166f5b0780426c4"
SESSION = "userbot_session"

client = TelegramClient(SESSION, API_ID, API_HASH)

def styled_clock():
    now = datetime.now().strftime("%H:%M:%S")
    style = f"⏰ [{now}] ⏰"
    return style

@client.on(events.NewMessage(pattern="licka", incoming=True))
async def auto_reply(event):
    reply_text = f"Salom 😊\nMana hozirgi vaqt: {styled_clock()}"
    await event.reply(reply_text)

async def main():
    print("✅ Userbot ishlayapti...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
