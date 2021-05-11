from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db
from utils.misc import rate_limit
import asyncpg


@rate_limit(limit=5)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        await db.add_user(id=message.from_user.id,Name=name)
    except asyncpg.exceptions.UniqueViolationError:
        pass
    count = await db.count_users()
    await message.answer(
        "\n".join([
            f'Hello, <b>{message.from_user.full_name}!</b>',
            f'In database <b>{count}</b> users',
            f'Click /menu to get bot menu',
            f'Click /help to get help'
        ])
    )