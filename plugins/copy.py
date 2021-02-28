from pyrogram import (
    Client,
    filters
    )


@Client.on_message(filters.private & ~filters.caption &
                   ~filters.command("start") & filters.user([1635529094,607489181,1009049027,1692084506,1582414817,1172718764,1635529094,1022465446,1480898794,1013812153,1138549080,1138549080,1100693020,1144861994,933142933,1153483615,1214799927]))
async def copy(client, message):
    chat = message.chat.id
    await message.copy(chat)
