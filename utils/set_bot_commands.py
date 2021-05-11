from aiogram.types import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand('start', 'Start Bot'),
        BotCommand('help', 'Helper'),
        BotCommand('menu', 'Bots menu'),
        BotCommand('quiz', 'Quick test'),
        BotCommand('get_crypto_price', 'Get cryptocurrency price'),
        BotCommand('show_on_map', 'Show nearest crypto exchangers')
    ])