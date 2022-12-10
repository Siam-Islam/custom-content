from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private & filters.command(['start']))
async def start(_, m: Message):
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.'
    ) 
