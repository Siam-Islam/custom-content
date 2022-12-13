from pyrogram import Client as app, filters

@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    await message.reply('Hi, Send me a file to get an instant stream link.')

@app.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def doc(client, message):
    await message.reply(f"""What do you want me to do with this file?""",reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename", callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel", callback_data = "cancel")  ]]))
