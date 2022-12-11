from pyrogram import filters, Client, Message

@Client.on_message(filters.private & filters.command(['start']))
async def start(_, m: Message):
    await m.reply('Hi I am working.') 
