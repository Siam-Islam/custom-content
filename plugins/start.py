import humanize
from pyrogram.file_id import FileId
from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    await message.reply('Hi, Send me a file to get an instant stream link.')

@app.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    media = await client.get_messages(message.chat.id, message.message_id)
    file = media.document or media.video or media.audio
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply(f"""What do you want me to do with this file?\n**File Name** :- {filename}\n**File Size** :- {filesize}""",reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename", callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel", callback_data = "cancel")  ]]))
