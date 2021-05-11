from utils.set_bot_commands import set_default_commands
from utils.db_api.database import create_db
from loader import db


async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)
    await create_db()
    
    await db.create_table_users()
    await db.delete_users()
    

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)


