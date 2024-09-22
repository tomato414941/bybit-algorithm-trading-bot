# check_positions.py

from pybit.unified_trading import HTTP
from tabulate import tabulate

from config import settings


def get_positions():
    session = HTTP(
        testnet=settings.USE_TESTNET,
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET,
    )

    try:
        response = session.get_positions(category="linear", symbol=settings.SYMBOL)
        return response["result"]["list"]
    except Exception as e:
        print(f"Error fetching positions: {e}")
        return []


def format_positions(positions):
    formatted = []
    for position in positions:
        formatted.append(
            [
                position["symbol"],
                position["side"],
                position["size"],
                position["avgPrice"],
                position["unrealisedPnl"],
                position["leverage"],
            ]
        )
    return formatted


def main():
    positions = get_positions()

    if not positions:
        print("No open positions found.")
        return

    formatted_positions = format_positions(positions)

    headers = ["Symbol", "Side", "Size", "Entry Price", "Unrealized PnL", "Leverage"]
    print(tabulate(formatted_positions, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
