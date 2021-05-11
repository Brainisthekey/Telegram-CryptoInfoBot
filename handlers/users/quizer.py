from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import Test



@dp.message_handler(Command("quiz"), state=None)
async def enter_test(message: types.Message, state: FSMContext):
    await message.answer(text=
                            "You just start testing\n"
                            "Question №1. \n\n"
                            "<b>Bitcoin pracie will increase in next 5 years ?</b>"
    )
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Question №2. \n\n"
                         "<b>Did you inwest in crypto some money ?</b>")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Thanks for your answer. Chears!")
    await message.answer(f"Your answer is : \n {answer1}\n {answer2}")

    await state.finish()
