import requests, re, asyncio, humanize
from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

s = requests.Session()

class utilities:
    def is_url(text):
        return text.startswith("http")

    async def get_filename(file_link):
       r = s.get(file_link, allow_redirects=True, stream=True)
       cd = r.headers.get("content-disposition")
       if not cd:
           return "None"
       fname = re.findall("filename=(.+)", cd)
       name = fname[0]
       return name

    async def get_filesize(file_link):
       r = s.get(file_link, allow_redirects=True, stream=True)
       filesize = r.headers.get("Content-Length", 0)
       return filesize

@app.on_message(filters.private & filters.text)
async def url(client, message):
    if not utilities.is_url(message.text):
        return
    snt = await message.reply("Processing link.......")
    file_link = message.text
    name = await utilities.get_filename(file_link)
    bytes = await utilities.get_filesize(file_link)
    size = humanize.naturalsize(bytes, binary=True)
    if name == "None":
        await snt.edit_text("Unsupported link!")
    else:
        await snt.edit_text(f"Title: {name[1:][:-1]}\nSize: {size}", reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("Upload" , callback_data = "Upload") ], [InlineKeyboardButton("Subscribe", callback_data = "Cancel") ]]))

