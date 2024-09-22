# strategies/sma_strategy.py

import numpy as np

from config import settings


class SimpleMovingAverageCrossover:
    def __init__(self, market_data):
        self.market_data = market_data

    def calculate_signal(self):
        kline = self.market_data.get_kline(settings.SYMBOL, interval="1")
        closes = np.array([float(candle[4]) for candle in kline])

        fast_ma = np.mean(closes[-settings.FAST_MA_PERIOD :])
        slow_ma = np.mean(closes[-settings.SLOW_MA_PERIOD :])

        if fast_ma > slow_ma:
            return "BUY"
        elif fast_ma < slow_ma:
            return "SELL"
        else:
            return "HOLD"
