# trading/order.py

from config import settings
from trading.exchange import BybitExchange
from utils.logger import logger


class OrderManager:
    def __init__(self):
        self.exchange = BybitExchange()

    def execute_trade(self, signal):
        positions = self.exchange.get_positions()
        position = next((p for p in positions if p["symbol"] == settings.SYMBOL), None)
        current_position = (
            float(position["size"]) if position and position["size"] else 0.0
        )

        logger.info(f"Current position size: {current_position}")

        try:
            if signal == "BUY":
                if current_position <= 0:
                    logger.info("Placing BUY order")
                    self.exchange.place_order("Buy", settings.QUANTITY)
                else:
                    logger.info("Already in a BUY position")
            elif signal == "SELL":
                if current_position >= 0:
                    logger.info("Placing SELL order")
                    self.exchange.place_order("Sell", settings.QUANTITY)
                else:
                    logger.info("Already in a SELL position")
            else:
                logger.info("No trade action for HOLD signal")
        except Exception as e:
            logger.error(f"Error executing trade: {e}")
