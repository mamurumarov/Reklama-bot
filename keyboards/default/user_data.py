from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="ID"), KeyboardButton(text="Username")],
        [KeyboardButton(text="First Name"), KeyboardButton(text="Last Name")]
    ]
)