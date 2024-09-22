# fetch_historical_data.py

import os
from datetime import datetime, timedelta

import pandas as pd
from pybit.unified_trading import HTTP

from config import settings


def fetch_historical_data(
    symbol: str, interval: str, start_time: datetime, end_time: datetime = None
):
    session = HTTP(
        testnet=settings.USE_TESTNET,
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET,
    )

    if end_time is None:
        end_time = datetime.now()

    all_klines = []
    current_time = start_time

    while current_time < end_time:
        try:
            response = session.get_kline(
                category="linear",
                symbol=symbol,
                interval=interval,
                start=int(current_time.timestamp() * 1000),
                end=int(
                    min(current_time + timedelta(days=30), end_time).timestamp() * 1000
                ),
                limit=1000,
            )
            klines = response["result"]["list"]
            all_klines.extend(klines)

            if not klines:
                break

            current_time = datetime.fromtimestamp(int(klines[0][0]) / 1000) + timedelta(
                minutes=1
            )
        except Exception as e:
            print(f"Error fetching data: {e}")
            break

    df = pd.DataFrame(
        all_klines,
        columns=["timestamp", "open", "high", "low", "close", "volume", "turnover"],
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    df = df.astype(float)
    df.sort_index(inplace=True)

    return df


def save_to_csv(df: pd.DataFrame, symbol: str, interval: str):
    data_dir = os.path.join(os.path.dirname(__file__), "historical_data")
    os.makedirs(data_dir, exist_ok=True)

    start_date = df.index[0].strftime("%Y%m%d")
    end_date = df.index[-1].strftime("%Y%m%d")
    filename = f"{symbol}_{interval}m_{start_date}_{end_date}.csv"
    filepath = os.path.join(data_dir, filename)

    df.to_csv(filepath)
    print(f"Data saved to {filepath}")


if __name__ == "__main__":
    symbol = settings.SYMBOL
    interval = "1"  # 1 minute
    start_time = datetime.now() - timedelta(days=30)  # Last 30 days

    df = fetch_historical_data(symbol, interval, start_time)
    save_to_csv(df, symbol, interval)

    print(df.head())
    print(f"Total rows: {len(df)}")
