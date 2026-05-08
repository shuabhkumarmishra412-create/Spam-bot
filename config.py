import logging

from telethon import TelegramClient

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = ""
API_HASH = ""
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

BOT_TOKEN = getenv("", default=None)
BOT_TOKEN2 = getenv("", default=None)
BOT_TOKEN3 = getenv("", default=None)
BOT_TOKEN4 = getenv("", default=None)
BOT_TOKEN5 = getenv("", default=None)
BOT_TOKEN6 = getenv("", default=None)
BOT_TOKEN7 = getenv("", default=None)
BOT_TOKEN8 = getenv("", default=None)
BOT_TOKEN9 = getenv("", default=None)
BOT_TOKEN10 = getenv("", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8441236350"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

