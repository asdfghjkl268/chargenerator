from aiogram import Bot, Dispatcher, executor, types
from settling import tok

bot = Bot(token=tok)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hi(message: types.Message):
    await message.reply("Hi!\nI'm stupid bot for generating dnd characters")

if __name__ == '__main__':
  executor.start_polling(dp)
