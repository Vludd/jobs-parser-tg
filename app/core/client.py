import asyncio
from app.config import SEND_TO, WHITELIST, BLACKLIST
from app.dependencies import CLIENT, PARSING_TARGETS

import logging

def start():
    if not PARSING_TARGETS:
        logging.error(f"Target list is empty! Nothing to parse...")
        return
    
    if not SEND_TO:
        logging.warning("Send_to field is empty. Using 'me'...")
        
    if not WHITELIST:
        logging.warning("White list is empty!")
        
    if not BLACKLIST:
        logging.warning("White list is empty!")
    
    try:
        with CLIENT:
            logging.info("MTProto client started")
            CLIENT.run_until_disconnected()
    except asyncio.CancelledError:
        logging.debug("MTProto client cancelled")
