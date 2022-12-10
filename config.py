from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    API_ID = int(environ.get("API_ID", "2766365"))
    API_HASH = str(environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "5848398486:AAE5POD1kHSQC1F6eIhmzIyqdihUM2wDkVY"))
