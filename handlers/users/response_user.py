from cgitb import text
from aiogram import types
from loader import dp

@dp.message_handler(text="ID")
async def send_user_id(message: types.Message):
    id = message.from_user.id
    await message.answer(f"Sizning ID: {id}")



@dp.message_handler(text="Username")
async def send_username(message: types.Message):
    username = message.from_user.username
    await message.answer(f"Sizning Username: {username}")

@dp.message_handler(text="First Name")
async def send_firstname(message: types.Message):
    firstname = message.from_user.first_name
    await message.answer(f"sizning firstname: {firstname}")


@dp.message_handler(text="Last Name")
async def send_lastname(message: types.Message):
    lastname = message.from_user.last_name
    await message.answer(f"Sizning lastname: {lastname}")