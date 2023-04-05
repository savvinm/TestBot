import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt


def read_token():
    with open("token.txt", "r") as file:
        token = file.read()
        return token


def get_story():
    with open("story.txt", "r") as file:
        story = file.read()
        return story


def get_story_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="About love 😘😍", callback_data="story_love"),
        types.InlineKeyboardButton(text="About superheroes 🦸", callback_data="story_superheroes"),
        types.InlineKeyboardButton(text="About friendship 🤜🤛", callback_data="story_friendship")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard



bot = Bot(token=read_token())
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


# Method to response to 'start' command.
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Get a story", "Info"]
    keyboard.add(*buttons)
    await message.answer(
        fmt.text(
        fmt.text(fmt.hbold("Hello!"), " 👋 "),
        fmt.text("\n🤖 here to give you the best stories to read.")
        ), parse_mode="HTML", reply_markup=keyboard
    )


async def cmd_info(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub 🤓", url="https://github.com/savvinm"),
        types.InlineKeyboardButton(text="Contact me in Telegram 📟", url="t.me/tolorid")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer(fmt.hbold("About this Bot ℹ"), parse_mode="HTML", reply_markup=keyboard)


async def cmd_get_story(message: types.Message):
    await message.answer(fmt.hbold("Select your story 📖"), parse_mode="HTML", reply_markup=get_story_keyboard())


@dp.callback_query_handler(text="story_love")
async def send_story_love(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Get another one 📖", callback_data="another_one"))
    await call.message.answer(
        fmt.text(fmt.hbold("Here is your story about love:\n"), "\n" + get_story()
        ), parse_mode="HTML", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="story_superheroes")
async def send_story_superheroes(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Get another one 📖", callback_data="another_one"))
    await call.message.answer(
        fmt.text(fmt.hbold("Here is your story about superheroes:\n"), "\n" + get_story()
        ), parse_mode="HTML", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="story_friendship")
async def send_story_friendship(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Get another one 📖", callback_data="another_one"))
    await call.message.answer(
        fmt.text(fmt.hbold("Here is your story about friendship:"), "\n" + get_story()
        ), parse_mode="HTML", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="another_one")
async def another_one(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=fmt.hbold("Select your story 📖"), parse_mode="HTML", reply_markup=get_story_keyboard())
    await call.answer()


dp.register_message_handler(cmd_info, commands=["info"])
dp.register_message_handler(cmd_info, text="Info")

dp.register_message_handler(cmd_get_story, commands=["story"])
dp.register_message_handler(cmd_get_story, text="Get a story")


# Method to response to a text message.
@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    if message.text.lower() == "hello":
        await message.answer("Hello!")
    else:
        await message.answer(message.text)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)