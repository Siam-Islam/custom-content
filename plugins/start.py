from pyrogram import Client as app, filters

@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    await message.reply('Hi, Send me a file to get an instant stream link.')

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
	reply_markup=ForceReply(True)

@app.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def doc(client, message):
    await message.reply(f"""What do you want me to do with this file?""",reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename", callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel", callback_data = "cancel")  ]]))
