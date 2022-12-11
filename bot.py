import asyncio
import os
import logging
from aiohttp import web
from plugins import web_server
from pyrogram import Client, idle

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

BOT_TOKEN = os.environ.get("TOKEN", "1763065907:AAFk-ITNJWExRGAzCSGzKkchUTLqP7lHFxQ")
API_ID = os.environ.get("API_ID", "2766365")
API_HASH = os.environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef")
PORT= os.environ.get("PORT", "8000")
server = web.AppRunner(web_server())

if __name__ == "__main__" :
    app = Client("MYBot", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID, plugins={"root": "plugins"})
    app.start()
    print("Bot Started")
    idle()
    print("Bot Stopped")
