# data/market_data.py

from pybit.unified_trading import HTTP

from config import settings


class MarketData:
    def __init__(self):
        self.session = HTTP(
            testnet=settings.USE_TESTNET,
            api_key=settings.API_KEY,
            api_secret=settings.API_SECRET,
        )

    def get_ticker(self, symbol):
        response = self.session.get_tickers(category="linear", symbol=symbol)
        return response["result"]["list"][0]

    def get_kline(self, symbol, interval, limit=200):
        response = self.session.get_kline(
            category="linear", symbol=symbol, interval=interval, limit=limit
        )
        return response["result"]["list"]

    def get_orderbook(self, symbol):
        response = self.session.get_orderbook(category="linear", symbol=symbol)
        return response["result"]
