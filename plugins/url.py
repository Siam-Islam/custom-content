import requests, re
from pyrogram import Client as app, filters

SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

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

    def get_readable_file_size(size_in_bytes) -> str:
    if size_in_bytes is None:
        return '0B'
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        return f'{round(size_in_bytes, 2)}{SIZE_UNITS[index]}'
    except IndexError:
        return 'File too large'

@app.on_message(filters.private & filters.text)
async def url(client, message):
    if not Utilities.is_url(message.text):
        return
    snt = await message.reply("Hi Please wait while I'm getting everything ready to process your request!")
    file_link = message.text
    name = await Utilities.get_filename(file_link)
    bytes = await Utilities.get_filesize(file_link)
    size = get_readable_file_size(bytes)
    if isinstance(name, str):
        await snt.edit_text("😟 Sorry! I cannot open the file.")
        return
    await snt.edit_text(f"Title: {name}\nSize: {size}")
        

