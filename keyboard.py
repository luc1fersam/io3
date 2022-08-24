from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#from aiogram.types import Message
#from aiogram.dispatcher.filters import Command, Text


#replykeyboards
greeting_button = KeyboardButton('Hiii') 
parting_button = KeyboardButton('Byeee')

greeting_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(greeting_button, parting_button)


#inlinekeyboards

inlkeyboard1 = InlineKeyboardButton(text='text', callback_data='random no 1')
inlkeyboard2 = InlineKeyboardButton(text='text', callback_data='random no 2')

keyboard_inline = InlineKeyboardMarkup().add(inlkeyboard1, inlkeyboard2)

