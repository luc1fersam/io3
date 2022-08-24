from main import bot, dp 

from aiogram.types import Message
from config import admin_id, moderator_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='bot is polling')
    await bot.send_message(chat_id=moderator_id, text='bot is polling')
    