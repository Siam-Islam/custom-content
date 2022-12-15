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
       if len(filename) == 0:
           return None
       return filename[0]

@app.on_message(filters.private & filters.text)
async def url(client, message):
    if not Utilities.is_url(message.text):
        return
    snt = await message.reply("Hi Please wait while I'm getting everything ready to process your request!")
    file_link = message.text
    name = await Utilities.get_filename(file_link)
    if isinstance(name, str):
        await snt.edit_text("😟 Sorry! I cannot open the file.")
        return
    await snt.edit_text(text=f"{name}")
        

