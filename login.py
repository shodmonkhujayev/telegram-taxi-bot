import asyncio

from telethon import TelegramClient
from app.config import config


async def main():
    client = TelegramClient(
        "session",
        config.API_ID,
        config.API_HASH,
    )

    await client.start()

    print("Authorized:", await client.is_user_authorized())

    me = await client.get_me()
    print("Logged in as:", me.first_name)

    await client.disconnect()


asyncio.run(main())
