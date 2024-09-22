# check_bybit_api_responses.py

from pybit.unified_trading import HTTP

from config import settings

SYMBOL = settings.SYMBOL


def main():
    session = HTTP(
        testnet=settings.USE_TESTNET,
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET,
    )

    try:
        kline_response = session.get_kline(
            category="linear", symbol=SYMBOL, interval="1", limit=5
        )
        print("Kline Response:")
        print(kline_response)
    except Exception as e:
        print(f"Error fetching kline data: {e}")

    try:
        ticker_response = session.get_tickers(category="linear", symbol=SYMBOL)
        print("\nTicker Response:")
        print(ticker_response)
    except Exception as e:
        print(f"Error fetching ticker data: {e}")

    try:
        orderbook_response = session.get_orderbook(category="linear", symbol=SYMBOL)
        print("\nOrderbook Response:")
        print(orderbook_response)
    except Exception as e:
        print(f"Error fetching orderbook data: {e}")

    try:
        position_response = session.get_positions(category="linear", symbol=SYMBOL)
        print("\nPosition Response:")
        print(position_response)
    except Exception as e:
        print(f"Error fetching position data: {e}")


if __name__ == "__main__":
    main()
