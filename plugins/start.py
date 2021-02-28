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


@Client.on_message(filters.command('start') & filters.private & filters.user([1635529094,607489181,1009049027,1692084506,1582414817,1172718764,1635529094,1022465446,1480898794,1013812153,1138549080,1138549080,1100693020,1144861994,933142933,1153483615,1214799927]))
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
