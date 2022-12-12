from bot import app
from pyrogram import filters

@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    await message.reply('Hi, Send me a file to get an instant stream link.')
