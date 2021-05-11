from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


price_cryptocurrency = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='💸BTCUSD'), KeyboardButton(text='💸ETHUSD')
        ],
        [
            KeyboardButton(text='💸XRPUSD'), KeyboardButton(text='💸BNBUSD')
        ]
    ],
    resize_keyboard=True
)