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
     file = update.message.reply_to_message
     ms = await update.message.edit("Trying To Download...")
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=("Trying To Download...",  ms, time.time()))
     except Exception as e:
     	await ms.edit(e)
     	return
     splitpath = path.split("/downloads/")
     await ms.edit("Trying To Upload")
     try:
     	 await bot.send_document(update.message.chat.id,document = file_path,caption = f"**{new_filename}**",progress=progress_for_pyrogram,progress_args=( "Trying To Uploading", ms, time.time()))
     	 await ms.delete()
     	 os.remove(file_path)				
     except Exception as e:
     	 await ms.edit(e)
     	 os.remove(file_path)
     
     		
