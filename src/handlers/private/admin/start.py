from aiogram import Router, types
from aiogram.filters import Command, Text

router = Router()


@router.message(Command(commands=['start']))
async def on_start(message: types.Message):
    text = 'Привет админ'
    await message.answer(text)
