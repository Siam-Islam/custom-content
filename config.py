from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    API_ID = int(environ.get("API_ID", "2766365"))
    API_HASH = str(environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "1763065907:AAEtGmMbHR8lZTY5xn0XYtm9JWAp_Zga0OY"))
