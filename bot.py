import os, asyncio, logging
from aiohttp import web
from pyrogram import Client, filters, idle

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)

bot_token = os.environ.get("TOKEN", "1763065907:AAFk-ITNJWExRGAzCSGzKkchUTLqP7lHFxQ")
api_id = os.environ.get("API_ID", "2766365")
api_hash = os.environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef")
port = os.environ.get("PORT", "8000")
loop = asyncio.get_event_loop()
routes = web.RouteTableDef()
app = Client("my_bot", bot_token = bot_token, api_hash = api_hash, api_id = api_id, plugins = {"root": "plugins"})

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello world")

def web_server():
    web_app = web.Application()
    web_app.add_routes(routes)
    return web_app

server = web.AppRunner(web_server())

async def start_services():
    await app.start()
    await server.setup()
    await web.TCPSite(server, "0.0.0.0", port).start()
    await idle  

if __name__ == "__main__":
    try:
        loop.run_until_complete(start_services())
    except Exception as e:
        logging.error(e.with_traceback(None))
        loop.stop()
        print("--BOT WAS UNABLE TO START--")
