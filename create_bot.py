from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

storage = MemoryStorage()

bot = Bot(token=config.TOKEN, , parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
