from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Поиск книги')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard= True)

kb_client.add(b1)