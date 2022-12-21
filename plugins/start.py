from pyrogram import Client, filters

@app.on_message(filters.command(["start"]))
async def echo(client, message):
    await message.reply("Hello")
