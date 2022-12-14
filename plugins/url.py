from pyrogram import Client as app, filters

class Utilities:
    def is_url(text):
        return text.startswith("http")

@app.on_message(filters.private & filters.text)
async def _(client, message):
    if not Utilities.is_url(message.text):
        return
    await message.reply_text("Hi there, Please wait while I'm getting everything ready to process your request!", quote=True,)
