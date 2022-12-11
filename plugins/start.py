from pyrogram import filters, Client, Message

@Client.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(f'Hi, Send me a file to get an instant stream link.')
