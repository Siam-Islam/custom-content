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

