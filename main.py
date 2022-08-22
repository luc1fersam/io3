import requests
API_link = 'https://api.telegram.org/bot5592228507:AAGR8XFmXqNdMgYdnvd4THD4B0lfgpJ-BfM'


updates = requests.get(API_link + '/getUpdates?offset=-1').json()


import logging

from config import TOKEN, admin_id

import keyboard as kb

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

#keyboard actions
@dp.message_handler(commands=['hi'])
async def greetings_kb(message: types.Message):

    await message.reply('Hello!', reply_markup=kb.greeting_keyboard)


#some talk actions

from commands import list_of_commands as loc
@dp.message_handler(commands=['help'])
async def commands_list(message: types.Message):

    await message.reply(f'Above you can see a list of available commands! {loc}')

@dp.message_handler(commands=['start'])
async def greetings(message: types.Message):
    
    await message.answer('Hi, Im apepepaieie bot!, send me /help and check list of commands')

@dp.message_handler()
async def echo(message: types.Message):
    
    await message.answer(message.text)




#admin messages must be above...


if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)