from .bot import app
from pyrogram.types import filters

@app.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    await message.reply('Hi I am working.') 
