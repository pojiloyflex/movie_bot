import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import movies
import nav
import strings

load_dotenv()
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           strings.greeting_phrase
                           .format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    response = movies.movie_collection.get(message.text.lower())
    if message.text == nav.btnShowCollectionText:
        await message.answer(movies.get_movie_collection())
    elif response is not None:
        await message.reply(response.get_text())
    else:
        await message.reply(strings.movie_not_found)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
