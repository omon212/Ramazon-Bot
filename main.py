import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = "6748487075:AAFWCHTJ1WmV7kl-SY2L8xSQNIMyh3kyeQA"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands="start")
async def starter(message:types.Message):
    await message.answer()