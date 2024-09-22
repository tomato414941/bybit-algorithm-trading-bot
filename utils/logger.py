# utils/logger.py

import logging

from config import settings


def setup_logger():
    logger = logging.getLogger("TradingBot")
    logger.setLevel(settings.LOG_LEVEL)

    if not logger.handlers:
        file_handler = logging.FileHandler(settings.LOG_FILE)
        file_handler.setLevel(settings.LOG_LEVEL)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger


logger = setup_logger()
