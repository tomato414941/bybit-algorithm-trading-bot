# utils/risk_management.py

from config import settings
from trading.exchange import BybitExchange
from utils.logger import logger


class RiskManager:
    def __init__(self):
        self.exchange = BybitExchange()

    def check_risk(self):
        positions = self.exchange.get_positions()
        position = next((p for p in positions if p["symbol"] == settings.SYMBOL), None)

        if not position or float(position["size"]) == 0:
            logger.info("No open positions.")
            return "NO_POSITION"

        current_position = float(position["size"])
        entry_price = float(position["avgPrice"]) if position["avgPrice"] else 0.0

        if entry_price == 0.0:
            logger.warning("Entry price is 0.0, cannot calculate PnL.")
            return "INVALID_ENTRY_PRICE"

        ticker = self.exchange.session.get_tickers(
            category="linear", symbol=settings.SYMBOL
        )
        current_price = float(ticker["result"]["list"][0]["lastPrice"])

        if position["side"] == "Buy":
            pnl_percent = (current_price - entry_price) / entry_price * 100
        elif position["side"] == "Sell":
            pnl_percent = (entry_price - current_price) / entry_price * 100
        else:
            pnl_percent = 0.0

        logger.info(f"PnL percent: {pnl_percent}%")

        if abs(pnl_percent) >= settings.STOP_LOSS_PERCENT:
            logger.info("Stop loss threshold reached, closing position.")
            self.exchange.place_order(
                "Sell" if position["side"] == "Buy" else "Buy",
                abs(current_position),
                reduce_only=True,
            )
            return "STOP_LOSS_TRIGGERED"

        if abs(pnl_percent) >= settings.TAKE_PROFIT_PERCENT:
            logger.info("Take profit threshold reached, closing position.")
            self.exchange.place_order(
                "Sell" if position["side"] == "Buy" else "Buy",
                abs(current_position),
                reduce_only=True,
            )
            return "TAKE_PROFIT_TRIGGERED"

        return "RISK_OK"
