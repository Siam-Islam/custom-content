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
    r = requests.get(message, allow_redirects=True, stream=True)
    cd = r.headers.get('content-disposition')
    if not cd:
        return None
    filename = re.findall('filename=(.+)', cd)
    if len(filename) == 0:
        return None
    return filename[0]
    await message.reply("Hi {filename}, Please wait while I'm getting everything ready to process your request!")
