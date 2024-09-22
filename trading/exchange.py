# trading/exchange.py

from pybit.unified_trading import HTTP

from config import settings
from utils.logger import logger


class BybitExchange:
    def __init__(self):
        self.session = HTTP(
            testnet=settings.USE_TESTNET,
            api_key=settings.API_KEY,
            api_secret=settings.API_SECRET,
        )

    def place_order(self, side, quantity, price=None, reduce_only=False):
        try:
            logger.info(
                f"Attempting to place order: Side={side}, Quantity={quantity}, Price={price}"
            )

            order_type = "Market" if price is None else "Limit"
            params = {
                "category": "linear",
                "symbol": settings.SYMBOL,
                "side": side,
                "orderType": order_type,
                "qty": str(quantity),
                "timeInForce": "GoodTillCancel",
                "reduceOnly": reduce_only,
                "closeOnTrigger": reduce_only,
            }
            if price is not None:
                params["price"] = str(price)

            response = self.session.place_order(**params)
            logger.info(f"Order response: {response}")

            if response.get("retCode") == 0:
                logger.info("Order placed successfully")
                return response
            else:
                logger.error(f"Order failed: {response.get('retMsg')}")
                return None
        except Exception as e:
            logger.error(f"Error placing order: {e}")
            return None

    def get_positions(self):
        try:
            response = self.session.get_positions(
                category="linear", symbol=settings.SYMBOL
            )
            return response["result"]["list"]
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return []
