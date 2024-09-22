# bybit-algorithm-trading-bot

bybit-algorithm-trading-bot is an automated cryptocurrency trading bot designed to work with the Bybit exchange. This bot is built in Python and uses the Bybit API to execute algorithmic trading strategies.

## Features

- Integration with Bybit API
- Real-time market data fetching and analysis
- Simple Moving Average Crossover strategy
- Automated order execution
- Risk management with stop-loss and take-profit
- Comprehensive logging and monitoring
- Historical data fetching and storage

## Prerequisites

- Python 3.8+
- Bybit account with API access

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bybit-algorithm-trading-bot.git
   cd bybit-algorithm-trading-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Bybit API credentials:
   ```
   cp config/settings.example.py config/settings.py
   ```
   Then edit `config/settings.py` and add your Bybit API key and secret.

## Project Structure

```
bybit-algorithm-trading-bot/
│
├── config/
│   ├── __init__.py
│   ├── settings.example.py   # Example configuration file
│   └── settings.py           # Actual configuration file (gitignored)
│
├── data/
│   ├── __init__.py
│   └── market_data.py        # Market data fetching and processing
│
├── strategies/
│   ├── __init__.py
│   └── sma_strategy.py       # Simple Moving Average Crossover strategy
│
├── trading/
│   ├── __init__.py
│   ├── exchange.py           # Interaction with Bybit API
│   └── order.py              # Order management
│
├── utils/
│   ├── __init__.py
│   ├── logger.py             # Logging functionality
│   └── risk_management.py    # Risk management utilities
│
├── historical_data/          # Directory for storing historical data (gitignored)
│
├── logs/                     # Directory for storing log files (gitignored)
│
├── check_account_balance.py  # Utility to check account balance
├── check_bybit_api_responses.py  # Utility to check API responses
├── check_positions.py        # Utility to check current positions
├── fetch_historical_data.py  # Script to fetch and save historical data
├── main.py                   # Main entry point
├── requirements.txt          # Dependencies
├── .gitignore                # Git ignore file
└── README.md                 # Project description
```

## Usage

1. Configure the bot:
   ```
   cp config/settings.example.py config/settings.py
   ```
   Edit `config/settings.py` with your Bybit API credentials and desired settings.

2. Fetch historical data:
   ```
   python fetch_historical_data.py
   ```

3. To start the trading bot, run:
   ```
   python main.py
   ```

## Configuration

You can configure the bot's behavior by editing the `config/settings.py` file. This includes:

- Bybit API credentials
- Trading symbol
- Leverage and quantity
- Strategy parameters (Fast and Slow MA periods)
- Risk management settings (Stop Loss and Take Profit percentages)
- Logging settings

## Strategy

The bot currently implements a Simple Moving Average (SMA) Crossover strategy in `strategies/sma_strategy.py`. It compares a fast SMA to a slow SMA to generate buy and sell signals.

## Risk Management

The bot includes basic risk management features:
- Stop Loss: Closes the position if the loss exceeds a specified percentage.
- Take Profit: Closes the position if the profit exceeds a specified percentage.

## Utilities

- `check_account_balance.py`: Use this script to check your account balance.
- `check_bybit_api_responses.py`: Use this script to test API responses for various data endpoints.
- `check_positions.py`: Use this script to check your current positions.
- `fetch_historical_data.py`: Use this script to fetch and save historical data.

## Logging

The bot logs all activities and errors to files in the `logs/` directory. The log file is specified in the `config/settings.py` file. You can adjust the log level and file path in the settings.

The `logs/` directory is automatically created when the bot runs. Log files are not tracked by git to avoid cluttering the repository.

## Disclaimer

This bot is for educational purposes only. Use it at your own risk. The authors are not responsible for any financial losses incurred from using this software. Always test thoroughly on a testnet before using real funds.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.