import os, asyncio, time, requests, re
from helper.progress import progress_for_pyrogram
from pyrogram import Client as app, filters
from pyrogram.types import ForceReply

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
async def doc(bot,update):
     url = "https://bashdora.ml/c4952910"
     name = await utilities.get_filename(url)
     new_filename = name[0]
     file_path = f"downloads/{new_filename[1:][:-1]}"
     ms = await update.message.edit("``` Trying To Download...```")
     c_time = time.time()
     try:
     	 path = await bot.download_media(message = url, progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     except Exception as e:
         await ms.edit(e)
     	 return
     	 await ms.edit("```Trying To Upload```")
     	 c_time = time.time()
     try:
         await bot.send_document(update.message.chat.id,document = file_path,caption = f"**{new_filename}**",progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
         await ms.delete()
         os.remove(file_path)
     except Exception as e:
         await ms.edit(e)
     	 os.remove(file_path)
     			     		   		
     		
   
     
     		
