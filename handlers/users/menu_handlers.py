from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from typing import Union
from data.config import photo
from loader import dp, bot
from keyboards.inline.menu_keyboards import categories_keyboard, subcategories_keyboard, menu_cd
from utils.db_api.db_commands import get_link


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await list_catigories(message)

async def list_catigories(message: Union[Message, CallbackQuery], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, Message):
        await bot.send_photo(
                            photo=photo,
                            chat_id=message.from_user.id,
                            reply_markup=markup
        )
    elif isinstance(message, CallbackQuery):
        await bot.send_photo(
                            photo=photo,
                            chat_id=message.from_user.id,
                            reply_markup=markup
        )


async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await callback.message.edit_reply_markup(markup)

async def next_step(callback: CallbackQuery, **kwargs):
    subcategory = kwargs['subcategory']
    if subcategory == 'Nearest Exhanger':
        await show_geo(callback, **kwargs)
    else:
        await show_btc(callback, **kwargs)

async def show_btc(callback: CallbackQuery, **kwargs):
    pair = kwargs['subcategory']
    link = await get_link(pair)
    text = f'You link is here:\n{link.photo}'
    if pair == "BTCUSDT":
        await bot.send_message(chat_id=callback.from_user.id, text=text)
    elif pair == "BNBUSDT":
        await bot.send_message(chat_id=callback.from_user.id, text=text)
    elif pair == "ETHUSDT":
        await bot.send_message(chat_id=callback.from_user.id, text=text)
    else:
        await bot.send_message(chat_id=callback.from_user.id, text=text)
    await callback.message.edit_reply_markup()
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

async def show_geo(callback: CallbackQuery, **kwargs):

    await callback.message.edit_reply_markup()
    await bot.send_message(
                          chat_id=callback.from_user.id,
                          text=
                                f'Hello, {callback.from_user.full_name}.\n'
                                f'If you want to know location nearest exchangers, I need your location \n'
                                f'Please press the /show_on_map !'
    )
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call:CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    link_id = int(callback_data.get('link_id'))

    levels = {
        "0" : list_catigories,
        "1" : list_subcategories,
        "2" : next_step
    }

    current_level_function = levels[current_level]
    await current_level_function(
        call,
        category=category,
        subcategory=subcategory,
        link_id=link_id,
    )