import os, asyncio, time
from helper.progress import progress_for_pyrogram
from pyrogram import Client as app, filters

@app.on_callback_query(filters.regex("cancel"))
async def cancel(bot,update):
        await update.message.delete()

@app.on_callback_query(filters.regex("doc"))
async def doc(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     ms = await update.message.edit_text("Trying To Download...")
     try:
     	 await bot.download_media(progress=progress_for_pyrogram,progress_args=("Trying To Download...",  ms, time.time()))
     except Exception as e:
     	 await ms.edit_text(e)
     	 return
     await ms.edit_text("Trying To Upload")
     try:
     	 await bot.send_document(update.message.chat.id,document = file_path,caption = f"**{new_filename}**",progress=progress_for_pyrogram,progress_args=( "Trying To Uploading", ms, time.time()))
     	 await ms.delete()
     	 os.remove(file_path)				
     except Exception as e:
     	 await ms.edit_text(e)
     	 os.remove(file_path)
     
     		
