import os, asyncio, time, requests, re
from helper.progress import progress_for_pyrogram
from pyrogram import Client as app, filters

s = requests.Session()

class utilities:
    async def get_filename(url):
       r = s.get(url, allow_redirects=True, stream=True)
       cd = r.headers.get("content-disposition")
       fname = re.findall("filename=(.+)", cd)
       name = fname[0]
       return name

@app.on_callback_query(filters.regex("cancel"))
async def cancel(bot, update):
        await update.message.delete()

@app.on_callback_query(filters.regex("doc"))
async def doc(bot, update):
     url = update.message.text
     name = await utilities.get_filename(url)
     file_path = f"downloads/{name[1:][:-1]}"
     ms = await update.message.edit("Trying To Download...")
     try:
     	 await bot.download_media(message = file_link, progress=progress_for_pyrogram,progress_args=("Trying To Download...",  ms, time.time()))
     except Exception as e:
     	 await ms.edit(e)
     await ms.edit_text("Trying To Upload")
     try:
     	 await bot.send_document(update.message.chat.id,document = file_path,caption = f"{name[1:][:-1]}" ,progress=progress_for_pyrogram,progress_args=( "Trying To Uploading", ms, time.time()))
     	 await ms.delete()
     	 os.remove(file_path)				
     except Exception as e:
     	 await ms.edit(e)
     	 os.remove(file_path)
     
     		
