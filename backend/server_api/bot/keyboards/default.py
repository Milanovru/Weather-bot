from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поделится локацией", request_location=True),
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)
