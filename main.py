import pytz
import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest




api_id = 3547639
api_hash = "2bf949e553081d817bd484640986c861"

time_texts = {
    1: "🕐", 2: "🕑", 3: "🕒", 4: "🕓", 5: "🕔", 6: "🕕", 7: "🕖", 8: "🕗", 9: "🕘",
    10: "🕙", 11: "🕚", 12: "🕛", 13: "🕐", 14: "🕑", 15: "🕒", 16: "🕓", 17: "🕔",
    18: "🕕", 19: "🕖", 20: "🕗", 21: "🕘", 22: "🕙", 23: "🕚", 0: "🕛"
}

timezone = pytz.timezone('Asia/Tehran')

async def update_profile():
    async with TelegramClient("datatimeviera", api_id, api_hash) as client:
        while True:
            try:
                now = datetime.now(timezone)
                hour = now.hour
                about_text = f"You will see this at {now.strftime('%H:%M')} {time_texts.get(hour, '')}"

                await client(UpdateProfileRequest(about=about_text))
                await asyncio.sleep(60 - now.second)
            except Exception as e:
                print(f"Error: {e}")
            finally:
                pass

if __name__ == "__main__":
    try:
        asyncio.run(update_profile())
    except KeyboardInterrupt:
        print("Execution interrupted.")
