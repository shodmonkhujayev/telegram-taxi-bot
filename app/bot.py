from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.config import config
from app.keyboards import main_menu

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🚖 Taxi Scanner Bot\n\n"
        "Xush kelibsiz!",
        reply_markup=main_menu
    )

