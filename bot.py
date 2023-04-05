import logging
from aiogram import Bot, Dispatcher, executor, types


def read_token():
    with open("token.txt", "r") as file:
        token = file.read()
        return token

def get_story():
    with open("story.txt", "r") as file:
        story = file.read()
        return story


bot = Bot(token=read_token())
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


# Method to response to 'start' command.
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Read a story", "Info"]
    keyboard.add(*buttons)
    await message.answer("Hello! 👋 \nI'am bot 🤖 and I'am here to give you the best stories to read.", reply_markup=keyboard)


async def cmd_info(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub 🤓", url="https://github.com/savvinm"),
        types.InlineKeyboardButton(text="Contact me in Telegram 📟", url="t.me/tolorid")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("About this Bot ℹ", reply_markup=keyboard)


async def cmd_get_story(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="About love 😘😍", callback_data="story_love"),
        types.InlineKeyboardButton(text="About superheroes 🦸", callback_data="story_superheroes"),
        types.InlineKeyboardButton(text="About friendship 🤜🤛", callback_data="story_friendship")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Select your story 📖", reply_markup=keyboard)


@dp.callback_query_handler(text="story_love")
async def send_story_love(call: types.CallbackQuery):
    await call.message.answer("Here is your story about love:\n" + get_story())
    await call.answer()


@dp.callback_query_handler(text="story_superheroes")
async def send_story_love(call: types.CallbackQuery):
    await call.message.answer("Here is your story about superheroes:\n" + get_story())
    await call.answer()


@dp.callback_query_handler(text="story_friendship")
async def send_story_love(call: types.CallbackQuery):
    await call.message.answer("Here is your story about friendship:\n" + get_story())
    await call.answer()


dp.register_message_handler(cmd_info, commands=["info"])
dp.register_message_handler(cmd_info, text="Info")

dp.register_message_handler(cmd_get_story, commands=["story"])
dp.register_message_handler(cmd_get_story, text="Read a story")

# Method to response to a text message.
@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    if message.text.lower() == "hello":
        await message.answer("Hello!")
    else:
        await message.answer(message.text)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)