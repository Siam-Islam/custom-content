import humanize, requests, re
from pyrogram.file_id import FileId
from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    url = https://bashdora.ml/c4952910
    r = requests.get(url, allow_redirects=True, stream=True)
    cd = r.headers.get('content-disposition')
    if not cd:
        return None
    filename = re.findall('filename=(.+)', cd)
    if len(filename) == 0:
        return None
    return filename[0]
    await message.reply(f"Hi, {filename} me a file to get an instant stream link.")

@app.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    media = await client.get_messages(message.chat.id, message.id)
    file = media.document or media.video or media.audio
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply(f"File Name: {filename}\nFile Size: {filesize}", reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename", callback_data = "rename"),InlineKeyboardButton("✖️ Cancel", callback_data = "cancel")]]))


@app.on_message(filters.command(["hi"]))
async def my_start(client, message):
    await message.reply(f'Hi, {info} Send me a file to get an instant stream link.')
    if not cd:
        return None
    filename = re.findall('filename=(.+)', cd)
    if len(filename) == 0:
        return None
    return filename[0]
