import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotSettings
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN, default=DefaultBotSettings(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("<b>👋 Welcome to your VIP bot!</b>", parse_mode=ParseMode.HTML)

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
