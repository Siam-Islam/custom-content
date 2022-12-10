import os
import logging
from plugins.stream import routes
from pyrogram import Client, idle

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

server = web.AppRunner(web_server())

def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_services():
    await web.TCPSite(server, 8000).start()

BOT_TOKEN = os.environ.get("TOKEN", "1763065907:AAEtGmMbHR8lZTY5xn0XYtm9JWAp_Zga0OY")
API_ID = int(os.environ.get("API_ID",2766365))
API_HASH = os.environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef")

if __name__ == "__main__" :
    plugins = dict(root="plugins")
    app = Client("MYBot", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID, plugins=plugins)
    logger.info("Bot Started")
    app.run()
    idle()
    logger.info("Bot Stopped")
