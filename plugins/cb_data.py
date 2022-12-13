import os, random, time
from helper.progress import humanbytes
from helper.progress import progress_for_pyrogram
from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

@app.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
		await update.message.delete()
	except:
		return

@app.on_callback_query(filters.regex('rename'))
async def rename(bot,update):
	chat_id = update.message.chat.id
	id = update.message.reply_to_message_id
	await update.message.delete()
	await update.message.reply_text(f"__Please enter the new filename...__\n\nNote:- Extension Not Required",reply_to_message_id = id,
	reply_markup=ForceReply(True) )

@app.on_callback_query(filters.regex("doc"))
async def doc(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     message = update.message.reply_to_message
     file = message.document or message.video or message.audio
     ms = await update.message.edit("```Trying To Download...```")
     c_time = time.time()
     try:
     	      path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     		
     except Exception as e:
          await ms.edit(e)
          return
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     caption = f"**{new_filename}**"
     
     value = 2090000000
     if value < file.file_size:
         await ms.edit("```Trying To Upload```")
         try:
             filw = await app.send_document(log_channel,document = file_path,thumb=ph_path,caption = caption,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
             from_chat = filw.chat.id
             mg_id = filw.id
             time.sleep(2)
             await bot.copy_message(update.from_user.id,from_chat,mg_id)
             await ms.delete()
             os.remove(file_path)
             try:
                 os.remove(ph_path)
             except:
                 pass
         except Exception as e:
             neg_used = used - int(file.file_size)
             used_limit(update.from_user.id,neg_used)
             await ms.edit(e)
             os.remove(file_path)
             try:
                 os.remove(ph_path)
             except:
                 return
     else:
     		await ms.edit("```Trying To Upload```")
     		c_time = time.time()
     		try:
     			await bot.send_document(update.from_user.id,document = file_path,thumb=ph_path,caption = caption,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))			
     			await ms.delete()
     			os.remove(file_path)
     		except Exception as e:
     			neg_used = used - int(file.file_size)
     			used_limit(update.from_user.id,neg_used)
     			await ms.edit(e)
     			os.remove(file_path)
     			return 
