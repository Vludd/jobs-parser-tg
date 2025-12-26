from app.core.client import start
from app.core.logger import setup_logger
import logging

if __name__ == "__main__":
    setup_logger(logging.INFO)
    start()
