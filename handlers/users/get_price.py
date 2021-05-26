from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from keyboards.inline.price_keyboards import price_cryptocurrency
from utils.get_price_crypto import get_price_c

@dp.message_handler(Command("get_crypto_price"))
async def show_on_map(message: Message):
    await message.answer(
        f'Hello, {message.from_user.full_name}.\n'
        f'If you want to know location nearest exchangers, I need your location \n'
        f'Please press the buttom!',
        reply_markup=price_cryptocurrency
    )

@dp.message_handler(Text(equals=["💸BTCUSD", "💸ETHUSD", "💸XRPUSD", "💸BNBUSD"]))
async def get_price(message: Message):
    if message.text == "💸BTCUSD":
        await message.answer(text = await message_to_send(currency='bitcoin'), reply_markup=ReplyKeyboardRemove())
    elif message.text == "💸ETHUSD":
        await message.answer(text = await message_to_send(currency='ethereum'),reply_markup=ReplyKeyboardRemove())
    elif message.text == "💸XRPUSD":
        await message.answer(text = await message_to_send(currency='xrp'), reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text = await message_to_send(currency='binance-coin'), reply_markup=ReplyKeyboardRemove())

async def message_to_send(currency: str):
    return f'Actuall price <b>{currency}: {get_price_c(currency=currency)}</b>'
