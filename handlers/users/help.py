from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List commands: ",
            "/start - Start bot",
            "/help - You need help ?",
            "/menu - Get bot menu",
            "/quiz - Quick test",
            "/get_crypto_price - Get cryptocurrency price",
            "/show_on_map - Show nearest crypto exhangers",
            "/email - Update info in database about you"
        )
    
    await message.answer("\n".join(text))
