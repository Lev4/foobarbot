from aiogram import Bot, Dispatcher, types
from aiogram import executor
from localconf import bot_token

bot = Bot(token=bot_token)

dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    if message.text == '/book':
        text = 'book!'
        await bot.send_message(chat_id, text)
    else:
        text = "Какой-то текст"
        await bot.send_message(chat_id, text)


executor.start_polling(dp)
