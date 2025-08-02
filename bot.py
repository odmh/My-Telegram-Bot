import os
from aiogram import Bot, Dispatcher, types, executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
BOT_USERNAME = os.getenv("BOT_USERNAME")
COFFEE_LINK = os.getenv("COFFEE_LINK")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.reply(f"Welcome! Join our channel {CHANNEL_ID} and support us here: {COFFEE_LINK}")

@dp.message_handler()
async def forward_to_channel(message: types.Message):
    if message.chat.type == "private":
        try:
            await bot.send_message(CHANNEL_ID, f"From @{message.from_user.username or message.from_user.id}:\n{message.text}")
            await message.reply("Your message has been forwarded!")
        except Exception as e:
            await message.reply("Failed to send your message.")

if __name__ == "__main__":
    executor.start_polling(dp)