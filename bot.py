import asyncio
import os
import logging
from plugins import web_server
from pyrogram import Client, idle

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

server = web.AppRunner(web_server())

BOT_TOKEN = os.environ.get("TOKEN", "1763065907:AAEtGmMbHR8lZTY5xn0XYtm9JWAp_Zga0OY")
API_ID = int(os.environ.get("API_ID",2766365))
API_HASH = os.environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef")
PORT= int(os.environ.get("PORT", 8000))
app = Client("MYBot", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID, plugins={"root": "plugins"})
loop = asyncio.get_event_loop()

async def start_services():
    print()
    print("-------------------- Initializing Telegram Bot --------------------")
    await app.start()
    bot_info = await app.get_me()
    app.username = bot_info.username
    print("------------------------------ DONE ------------------------------")
    await server.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(server, bind_address, PORT).start()
    print("------------------------------ DONE ------------------------------")
    print()
    print("------------------------- Service Started -------------------------")
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
        print("Stopped Services")
