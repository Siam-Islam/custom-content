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

BOT_TOKEN = os.environ.get("TOKEN", "1763065907:AAEtGmMbHR8lZTY5xn0XYtm9JWAp_Zga0OY")
API_ID = int(os.environ.get("API_ID",2766365))
API_HASH = os.environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef")
PORT= int(os.environ.get("PORT", 8000))
app = Client("MYBot", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID, plugins={"root": "plugins"})
loop = asyncio.get_event_loop()
server = web.AppRunner(web_server())

async def start_services():
    await app.start()
    await server.setup()
    await web.TCPSite(server, PORT).start()
    print("Bot Started")
    await idle()

async def cleanup():
    await server.cleanup()
    await app.stop()

if __name__ == "__main__":
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.error(err.with_traceback(None))
    finally:
        loop.run_until_complete(cleanup())
        loop.stop()
        print("Bot Stopped")
