# config/settings.example.py

import logging

# Bybit API Credentials
API_KEY = ""  # Enter your Bybit API key here
API_SECRET = ""  # Enter your Bybit API secret here

# Trading parameters
SYMBOL = "BTCUSDT"
LEVERAGE = 10
QUANTITY = 0.001  # Contract size

# Strategy parameters
FAST_MA_PERIOD = 10
SLOW_MA_PERIOD = 30

# Risk management
MAX_POSITION_SIZE = 1000
STOP_LOSS_PERCENT = 2
TAKE_PROFIT_PERCENT = 4

# Logging
LOG_LEVEL = logging.INFO
LOG_FILE = "logs/trading_bot.log"

# Testnet or live
USE_TESTNET = True  # Set to False for live trading

# Add any other configuration parameters below
