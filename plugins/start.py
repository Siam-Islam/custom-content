import os, random, time
from helper.progress import humanbytes
from helper.set import escape_invalid_curly_brackets
from helper.progress import progress_for_pyrogram
from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    await message.reply('Hi, Send me a file to get an instant stream link.')

@app.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    await message.reply(f"""What do you want me to do with this file?""",reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename", callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel", callback_data = "cancel")  ]]))

@app.on_callback_query(filters.regex("doc"))
async def doc(bot,update):
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
     user_id = int(update.message.chat.id)
     data = find(user_id)
     try:
         c_caption = data[1]
     except:
         pass
     thumb = data[0]
     if c_caption:
        doc_list= ["filename","filesize"]
        new_tex = escape_invalid_curly_brackets(c_caption,doc_list)
        caption = new_tex.format(filename=new_filename,filesize=humanbytes(file.file_size))
     else:
        caption = f"**{new_filename}**"
     if thumb:
     		ph_path = await bot.download_media(thumb)
     		Image.open(ph_path).convert("RGB").save(ph_path)
     		img = Image.open(ph_path)
     		img.resize((320, 320))
     		img.save(ph_path, "JPEG")
     		c_time = time.time()
     		
     else:
     		ph_path = None
     
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
     			     		   		
   		
     		     		     		
