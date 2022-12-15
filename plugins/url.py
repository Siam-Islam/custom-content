import requests, re, humanize
from pyrogram import Client as app, filters

class utilities:
    def is_url(text):
        return text.startswith("http")

    def get_filename(file_link):
       r = requests.get(file_link, allow_redirects=True, stream=True)
       cd = r.headers.get('content-disposition')
       filename = re.findall('filename=(.+)', cd)
       if filename:
           return filename
       return None

    def get_filesize(file_link):
       r = requests.get(file_link, allow_redirects=True, stream=True)
       filesize = r.headers.get("Content-Length", 0)
       if filesize:
           return filesize[0]
       return None

@app.on_message(filters.private & filters.text)
async def url(client, message):
    if not utilities.is_url(message.text):
        return
    snt = await message.reply("Hi Please wait while I'm getting everything ready to process your request!")
    file_link = message.text
    name = utilities.get_filename(file_link)
    bytes = utilities.get_filesize(file_link)
    size = humanize.naturalsize(bytes, binary=True)
    if isinstance(name, str):
        await snt.edit_text("😟 Sorry! I cannot open the file.")
        return
    await snt.edit_text(f"Title: {name}\nSize: {size}")
        

