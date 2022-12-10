import os
import logging
from config import Config
from pyrogram import Client

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":

    StreamBot = Client(
                name="custom-content",
                api_id=Config.API_ID,
                api_hash=Config.API_HASH,
                plugins={"root": "plugins"},
                bot_token=Config.BOT_TOKEN,)

    logger.info("Bot Started")
    StreamBot.run()
    idle()
    logger.info("Bot Stopped")

