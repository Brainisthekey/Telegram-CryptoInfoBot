from loader import dp, db
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import Message
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('email'))
async def get_email(message: Message, state: FSMContext):
    await message.answer("Can you write your email adress")
    #Таким вот образом без создавания отдельного класса с машиной состояния
    #Может назначить юзеру какой-то state
    await state.set_state('email')

@dp.message_handler(state='email')
async def enter_email(message: Message, state: FSMContext):
    email = message.text
    await db.update_user_email(email=email, id=message.from_user.id)
    user = await db.select_user(id=message.from_user.id)
    if user:
        await message.answer(
            'Database was update \n'
            'Info about you:\n'
            '<b>Id: {id}</b>\n'
            '<b>Name : {name}</b>\n'
            '<b>Email : {email}</b>\n'.format(**user)
        )
        await state.finish()
    else:
        await message.answer(text='If you want update your email, you must be in database\nPlease click /start')
        await state.finish()