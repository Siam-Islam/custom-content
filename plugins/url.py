import requests, re
from pyrogram import Client as app, filters

class Utilities:
    def is_url(text):
        return text.startswith("http")

    async def get_filename(file_link):
       r = requests.get(file_link, allow_redirects=True, stream=True)
       cd = r.headers.get('content-disposition')
       if not cd:
           return None
       filename = re.findall('filename=(.+)', cd)
       if filename:
           return filename
       return None

    async def get_filesize(file_link):
       r = requests.get(file_link, allow_redirects=True, stream=True)
       filesize = r.headers.get("Content-Length", 0)
       if filesize:
           return filesize
       return "Unable to get file size."

@app.on_message(filters.private & filters.text)
async def url(client, message):
    if not Utilities.is_url(message.text):
        return
    snt = await message.reply("Hi Please wait while I'm getting everything ready to process your request!")
    file_link = message.text
    name = await Utilities.get_filename(file_link)
    size = await Utilities.get_filesize(file_link)
    if isinstance(name, str):
        await snt.edit_text("😟 Sorry! I cannot open the file.")
        return
    await snt.edit_text(f"Title: {name}\nSize: {size}")
        

