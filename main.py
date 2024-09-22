# main.py

import time

from data.market_data import MarketData
from strategies.sma_strategy import SimpleMovingAverageCrossover
from trading.order import OrderManager
from utils.logger import logger
from utils.risk_management import RiskManager


def main():
    market_data = MarketData()
    strategy = SimpleMovingAverageCrossover(market_data)
    order_manager = OrderManager()
    risk_manager = RiskManager()

    while True:
        try:
            signal = strategy.calculate_signal()
            logger.info(f"Strategy signal: {signal}")

            risk_status = risk_manager.check_risk()
            logger.info(f"Risk status: {risk_status}")

            if risk_status in ["RISK_OK", "NO_POSITION"]:
                order_manager.execute_trade(signal)

            time.sleep(60)  # Wait for 1 minute before the next iteration
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            time.sleep(60)  # Wait for 1 minute before retrying


if __name__ == "__main__":
    main()
