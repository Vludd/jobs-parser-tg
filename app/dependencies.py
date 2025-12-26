from telethon import TelegramClient
from app.config import TARGET_BOTS, TARGET_CHANNELS
from app.config.mtproto import SESSION_NAME, API_ID, API_HASH
from app.utils.formatter import MessageFormatter

CLIENT = TelegramClient(SESSION_NAME, API_ID, API_HASH)
FORMATTER = MessageFormatter()

PARSING_TARGETS = TARGET_CHANNELS + TARGET_BOTS
