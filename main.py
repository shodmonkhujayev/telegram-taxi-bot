from app.config import config

print("=" * 60)
print("BOT_TOKEN =", repr(config.BOT_TOKEN))
print("API_ID    =", config.API_ID)
print("API_HASH  =", repr(config.API_HASH))
print("OWNER_ID  =", config.OWNER_ID)
print("=" * 60)

import app.handlers

from app.bot import bot, dp
from app.scanner import scanner

import asyncio


async def main():

    scanner_task = asyncio.create_task(scanner.start())

    await dp.start_polling(bot)

    await scanner_task


if __name__ == "__main__":
    asyncio.run(main())
