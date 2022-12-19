import os, asyncio, time, requests, re
from helper.progress import progress_for_pyrogram
from pyrogram import Client as app, filters

class utilities:
    async def get_filename(file):
       r = s.get(text, allow_redirects=True, stream=True)
       cd = r.headers.get("content-disposition")
       if not cd:
           return "None"
       fname = re.findall("filename=(.+)", cd)
       name = fname[0]
       return name

@app.on_callback_query(filters.regex("cancel"))
async def cancel(bot, update):
        await update.message.delete()

@app.on_callback_query(filters.regex("doc"))
async def doc(bot, update):
     file = update.message.text
     name = await utilities.get_filename(file)
     file_path = f"downloads/{name[1:][:-1]}"
     ms = await update.message.edit_text("Trying To Download...")
     try:
     	 await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=("Trying To Download...",  ms, time.time()))
     except Exception as e:
     	 await ms.edit_text(e)
     await ms.edit_text("Trying To Upload")
     try:
     	 await bot.send_document(update.message.chat.id,document = file_path,caption = "video.mp4" ,progress=progress_for_pyrogram,progress_args=( "Trying To Uploading", ms, time.time()))
     	 await ms.delete()
     	 os.remove(file_path)				
     except Exception as e:
     	 await ms.edit_text(e)
     	 os.remove(file_path)
     
     		
