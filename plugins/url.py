import os, asyncio, logging, random, requests, re
from pyrogram import Client as app, filters

log = logging.getLogger(__name__)

class Utilities:
    def is_url(text):
        return text.startswith("http")

@app.on_message(filters.private & filters.text)
async def url(client, message):
    if not Utilities.is_url(message.text):
        return
    await message.reply("Hi Please wait while I'm getting everything ready to process your request!")
