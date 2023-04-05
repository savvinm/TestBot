from aiogram import Bot, Dispatcher, executor, types


def read_token():
    with open("token.txt", "r") as file:
        token = file.read()
        return token


bot = Bot(token=read_token())
dp = Dispatcher(bot)


# Method to response to 'start' command.
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Hello! \nI'am bot and ready to help you")


# Method to response to a text message.
@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    if message.text.lower() == "hello":
        await message.answer("Hello!")
    else:
        await message.answer(message.text)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)