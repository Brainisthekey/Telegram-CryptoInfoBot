from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.default import location_buttons
from utils.misc.calc_distance import choose_shortest


@dp.message_handler(Command("show_on_map"))
async def show_on_map(message: types.Message):
    await message.answer(
        f'Hello, <b>{message.from_user.full_name}.</b>\n'
        f'If you want to know location nearest exchangers, I need your location \n'
        f'Please press the buttom!',
        reply_markup=location_buttons.keyboard
    )

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_exchangers = choose_shortest(location)

    text_format = "<b>Name of shop: {shop_name}</b>. <a href='{url}'>Google</a>\n<u>Distance from your location to the exchanger: {distance:.1f} km</u>"

    text = "\n\n".join(
        [
            text_format.format(shop_name=shop_name, url=url, distance=distance)
            for shop_name, distance, url, shop_location, url_image in closest_exchangers
        ]
    )

    await message.answer_photo(photo=closest_exchangers[0][4])
    await message.answer(f'Thanks!\n'
                        f'Latitude = {latitude}\n'
                        f'Longitude = {longitude}\n\n'
                        f'{text}',
                        disable_web_page_preview=True
    )
    for shop_name, distance, url, shop_location, url_image in closest_exchangers:
        await message.answer_location(
            latitude=shop_location['lat'], 
            longitude=shop_location['lon'])


