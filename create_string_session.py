import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

from app.config import config


async def main():
    # Mavjud session.session faylini ochamiz
    old_client = TelegramClient(
        "session",
        config.API_ID,
        config.API_HASH,
    )

    await old_client.connect()

    if not await old_client.is_user_authorized():
        print("❌ session.session avtorizatsiya qilinmagan.")
        return

    # Shu avtorizatsiyani StringSession ga ko'chiramiz
    string = StringSession.save(old_client.session)

    print("\n" + "=" * 60)
    print("SESSION_STRING")
    print("=" * 60)
    print(string)
    print("=" * 60)

    await old_client.disconnect()


asyncio.run(main())

