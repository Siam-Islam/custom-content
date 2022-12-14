import requests, re, asyncio, humanize
from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

s = requests.Session()

class utilities:
    async def get_filename(file_url):
       r = s.get(file_url, allow_redirects=True, stream=True)
       cd = r.headers.get("content-disposition")
       if not cd:
           return "None"
       fname = re.findall("filename=(.+)", cd)
       name = fname[0]
       return name

    async def get_filesize(file_url):
       r = s.get(file_url, allow_redirects=True, stream=True)
       filesize = r.headers.get("Content-Length", 0)
       return filesize

@app.on_message(filters.private & filters.text)
async def url(client, message):
    file_url = message.text
    if not file_url.startswith("https://") or file_url.startswith("http://"):
        return
    snt = await message.reply_text("Processing link.......", reply_to_message_id = message.id)
    name = await utilities.get_filename(file_url)
    bytes = await utilities.get_filesize(file_url)
    size = humanize.naturalsize(bytes, binary=True)
    if not name == "None":
        await snt.edit_text(f"Title: {name[1:][:-1]}\nSize: {size}", reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upload", callback_data = "doc"),InlineKeyboardButton("Cancel", callback_data = "cancel") ]]))
    else:
        await snt.edit_text("Unsupported link!")
  
        
