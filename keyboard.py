from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

#from aiogram.types import Message
#from aiogram.dispatcher.filters import Command, Text

greeting_button = KeyboardButton('Hiii') 
parting_button = KeyboardButton('Byeee')

greeting_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(greeting_button, parting_button)



