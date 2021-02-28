from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **Funney Mewat Material SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize**
A little gift for Mewat family by 
@Kushwahajee @hackersemperor
Now Enjoy bot !!!"""


if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
