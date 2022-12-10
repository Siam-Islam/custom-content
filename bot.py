from config import Config
from pyrogram import Client

StreamBot = Client(
    name="custom-content",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins={"root": "plugins"},
    bot_token=Config.BOT_TOKEN,
)
