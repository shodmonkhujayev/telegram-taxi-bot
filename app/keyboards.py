from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔍 Scan"),
        ],
        [
            KeyboardButton(text="🚕 Taksi"),
            KeyboardButton(text="📦 Pochta"),
        ],
        [
            KeyboardButton(text="📊 Status"),
            KeyboardButton(text="ℹ️ Yordam"),
        ],
    ],
    resize_keyboard=True,
)


scan_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="▶️ Izlash"),
        ],
        [
            KeyboardButton(text="⏹ Bekor qilish"),
        ],
        [
            KeyboardButton(text="📊 Status"),
        ],
        [
            KeyboardButton(text="⬅️ Asosiy menyu"),
        ],
    ],
    resize_keyboard=True,
)
