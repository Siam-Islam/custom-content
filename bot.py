import os, asyncio, logging
from aiohttp import web
from pyrogram import Client, idle

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

token = os.environ.get("TOKEN", "1763065907:AAFk-ITNJWExRGAzCSGzKkchUTLqP7lHFxQ")
api_id = os.environ.get("API_ID", "2766365")
api_hash = os.environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef")
app = Client("MYBot", bot_token=token, api_hash=api_hash, api_id=api_id, plugins={"root": "plugins"})
port = os.environ.get("PORT", "8000")
loop = asyncio.get_event_loop()
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello world")

def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

server = web.AppRunner(web_server())

async def start_services():
    print("----- CHECKING THE BOT -----")
    await app.start()
    await server.setup()
    await web.TCPSite(server, "0.0.0.0", port).start()
    print("--BOT STARTED SUCESSFULLY--")
    await idle()

async def ideal_services():
    print("--BOT WAS UNABLE TO START--")

if __name__ == "__main__":
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.error(err.with_traceback(None))
    finally:
        loop.run_until_complete(ideal_services())
        loop.stop()
