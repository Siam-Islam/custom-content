from pyrogram import filters
from pyrogram.types import Message
from bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.'
    )
