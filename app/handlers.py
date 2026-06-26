from aiogram import F
from aiogram.types import Message

from app.bot import dp
from app.keyboards import main_menu, scan_menu
from app.services.scan_service import scan_service


@dp.message(F.text == "🔍 Scan")
async def scan(message: Message):
    await message.answer(
        "🔍 Scanner boshqaruvi",
        reply_markup=scan_menu,
    )


@dp.message(F.text == "▶️ Izlash")
async def start_scan(message: Message):

    print("===== START HANDLER =====")

    started = await scan_service.start()

    print("STARTED =", started)

    if started:
        await message.answer("🟢 Scanner ishga tushdi.")
    else:
        await message.answer("⚠️ Scanner allaqachon ishlayapti.")


@dp.message(F.text == "⏹ Bekor qilish")
async def stop_scan(message: Message):

    print("===== STOP HANDLER =====")

    await scan_service.stop()

    await message.answer("🔴 Scanner to'xtatildi.")


@dp.message(F.text == "📊 Status")
async def status(message: Message):
    await message.answer(scan_service.status())


@dp.message(F.text == "🚕 Taksi")
async def taxi(message: Message):
    await message.answer("🚕 Taksi moduli ishlab chiqilmoqda.")


@dp.message(F.text == "📦 Pochta")
async def cargo(message: Message):
    await message.answer("📦 Pochta moduli ishlab chiqilmoqda.")


@dp.message(F.text == "ℹ️ Yordam")
async def help_menu(message: Message):
    await message.answer("ℹ️ Taxi Scanner\nVersion 1.0")


@dp.message(F.text == "⬅️ Asosiy menyu")
async def back(message: Message):
    await message.answer(
        "🏠 Asosiy menyu",
        reply_markup=main_menu,
    )

