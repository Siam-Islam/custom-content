from pyrogram import Client, idle
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

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
