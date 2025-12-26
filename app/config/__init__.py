from os import getenv
from pathlib import Path
from dotenv import load_dotenv
import json

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent # app dir
CONFIG_PATH = BASE_DIR / "config/config.json"

CONFIG_FILE: dict = json.load((CONFIG_PATH).open(encoding="utf-8"))

PRIVATE_CHANNEL: bool = getenv('PRIVATE_CHANNEL', "False").lower() == "true"

SEND_TO: str | int = ""
SEND_TO_RAW: str = getenv('SEND_TO_CHANNEL_ID', "me")

if SEND_TO_RAW:
    if SEND_TO_RAW.isdigit():
        SEND_TO = int(f"-100{SEND_TO_RAW}") if PRIVATE_CHANNEL else int(SEND_TO_RAW)
    else:
        SEND_TO = SEND_TO_RAW

TARGET_LIST: dict = CONFIG_FILE.get('targets', {})
FILTER_DICT: dict = CONFIG_FILE.get('filter', {})

TARGET_CHANNELS: list = TARGET_LIST.get('channels', [])
TARGET_BOTS: list = TARGET_LIST.get('bots', [])

WHITELIST: dict = FILTER_DICT.get('whitelist', {})
BLACKLIST: list = FILTER_DICT.get('blacklist', [])
TECH_STACK: dict = FILTER_DICT.get('techstack', {})
TECH_STACK: dict = FILTER_DICT.get('techstack', {})

TECH_MIN_SCORE: int = FILTER_DICT.get('min_score', 3)
