import config
import logging
import os

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

add_group_text = InlineKeyboardButton(text="➕ Guruhga qo'shish ➕", url="http://t.me/join_remover_uzbot?startgroup=new")
add_group = InlineKeyboardMarkup().add(add_group_text)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await message.answer("Salom 👋\n"
						 "Men guruhdagi yoki chatdagi kirdi-chiqdi xabarlarni o'chirib beraman 🧹🧹🧹."
						 "Men ishlashim uchun shunchaki meni guruh ADMINI qilishingiz kerak bo'ladi ✅.",
						 reply_markup=add_group)


@dp.message_handler(content_types=['new_chat_members', 'left_chat_member'])
async def delete(message: types.Message):
	await message.delete()


@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
	await message.delete()


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
