from os import getenv

from decouple import config
from telethon import TelegramClient

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
YOUR_NAME = config("YOUR_NAME", None)

bot = TelegramClient("LegendBoy", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
bot2 = TelegramClient("LegendBoy2", APP_ID, API_HASH).start(bot_token=BOT_TOKEN2)
bot3 = TelegramClient("LegendBoy3", APP_ID, API_HASH).start(bot_token=BOT_TOKEN3)
bot4 = TelegramClient("LegendBoy4", APP_ID, API_HASH).start(bot_token=BOT_TOKEN4)
bot5 = TelegramClient("LegendBoy5", APP_ID, API_HASH).start(bot_token=BOT_TOKEN5)
bot6 = TelegramClient("LegendBoy6", APP_ID, API_HASH).start(bot_token=BOT_TOKEN6)
bot7 = TelegramClient("LegendBoy7", APP_ID, API_HASH).start(bot_token=BOT_TOKEN7)
bot8 = TelegramClient("LegendBoy8", APP_ID, API_HASH).start(bot_token=BOT_TOKEN8)
bot9 = TelegramClient("LegendBoy9", APP_ID, API_HASH).start(bot_token=BOT_TOKEN9)
bot10 = TelegramClient("LegendBoy10", APP_ID, API_HASH).start(bot_token=BOT_TOKEN10)
