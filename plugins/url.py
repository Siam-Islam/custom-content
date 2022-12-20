import requests, re, asyncio, humanize
from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

s = requests.Session()

class utilities:
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
    https_link = message.startswith("https://")
    http_link = message.startswith("http://")
    if not https_link or http_link:
        return
    file_link = message.text
    snt = await message.reply("Processing link.......")
    name = await utilities.get_filename(file_link)
    bytes = await utilities.get_filesize(file_link)
    size = humanize.naturalsize(bytes, binary=True)
    await message.delete()
    if not name == "None":
        await snt.edit(f"Title: {name[1:][:-1]}\nSize: {size}", reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upload",callback_data = "doc"),InlineKeyboardButton("Cancel",callback_data = "cancel") ]]))
    else:
        await snt.edit("Unsupported link!")
  
        
