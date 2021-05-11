from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from utils.db_api.db_commands import get_categories, get_subcategories
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton

menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "link_id")

def make_callback_data(level, category="0", subcategory="0", link_id="0"):
    return menu_cd.new(
        level=level,
        category=category,
        subcategory=subcategory,
        link_id=link_id,
    )

async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)

    categories = await get_categories()
    for category in categories:
        button_text = f'{category.category_name}'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category.category_code)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup

async def subcategories_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=2)

    subcategories = await get_subcategories(category=category)
    for subcategory in subcategories:
        button_text = f"{subcategory.subcategory_name}"
        callback_data = make_callback_data(
                                        level=CURRENT_LEVEL + 1,
                                        category=category,
                                        subcategory=subcategory.subcategory_code,
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
        
    markup.row(
        InlineKeyboardButton(
                        text="Back",
                        callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup
