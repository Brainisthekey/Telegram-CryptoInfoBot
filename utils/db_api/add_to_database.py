from utils.db_api.db_commands import add_link
import asyncio
from utils.db_api.database import create_db

async def add_items():
    await add_link(name="Curency Exchangers",
                   category_name="💱 Curency Exchangers", category_code="Curency Exchangers",
                   subcategory_name="📍 Nearest Exhanger", subcategory_code="Nearest Exhanger",
                   photo="-")
    await add_link(name="BTCUSDT",
                   category_name="📈 Charts", category_code="Charts",
                   subcategory_name="📊 BTCUSDT", subcategory_code="BTCUSDT",
                   photo="https://pl.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT")
    await add_link(name="ETHUSDT",
                   category_name="📈 Charts", category_code="Charts",
                   subcategory_name="📊 ETHUSDT", subcategory_code="ETHUSDT",
                   photo="https://pl.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT")
    await add_link(name="XRPUSDT",
                   category_name="📈 Charts", category_code="Charts",
                   subcategory_name="📊 XRPUSDT", subcategory_code="XRPUSDT",
                   photo="https://pl.tradingview.com/chart/?symbol=BINANCE%3AXRPUSDT")
    await add_link(name="BNBUSDT",
                   category_name="📈 Charts", category_code="Charts",
                   subcategory_name="📊 BNBUSDT", subcategory_code="BNBUSDT",
                   photo="https://pl.tradingview.com/chart/?symbol=BINANCE%3ABNBUSDT")

def create_structue_database():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
    loop.run_until_complete(add_items())