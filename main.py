import asyncio

import app.handlers

from app.bot import bot, dp


async def main():

    print("=" * 60)
    print("🚖 Taxi Scanner Bot")
    print("✅ Bot started")
    print("=" * 60)

    try:
        await dp.start_polling(bot)

    except KeyboardInterrupt:
        print("\n🛑 Bot stopped")

    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
