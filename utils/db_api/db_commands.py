from re import M
from typing import List
from sqlalchemy.sql.elements import and_
from utils.db_api.models import MenuOptions
from utils.db_api.database import db


async def add_link(**kwargs):
    new_link = await MenuOptions(**kwargs).create()
    return MenuOptions

async def get_categories() -> List[MenuOptions]:
    return await MenuOptions.query.distinct(MenuOptions.category_code).gino.all()


async def get_subcategories(category) -> List[MenuOptions]:
    return await MenuOptions.query.distinct(MenuOptions.subcategory_code).where(MenuOptions.category_code == category).gino.all()

async def get_items(category_code, subcategory_code) -> List[MenuOptions]:
    item = await MenuOptions.query.where(
        and_(MenuOptions.category_code == category_code,
             MenuOptions.subcategory_code == subcategory_code)
    ).gino.all()
    return item

async def get_link(curency) -> MenuOptions:
    link = await MenuOptions.query.where(MenuOptions.name == curency).gino.first()
    return link

