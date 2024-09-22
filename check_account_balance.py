# check_account_balance.py

from pybit.unified_trading import HTTP

from config import settings


def main():
    session = HTTP(
        testnet=settings.USE_TESTNET,
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET,
    )

    try:
        balance_response = session.get_wallet_balance(
            accountType="UNIFIED", coin="USDT,BTC,ETH"
        )
        print("Balance Response:")
        print(balance_response)

        if balance_response["retCode"] != 0:
            print(f"Error fetching balance: {balance_response['retMsg']}")
            return

        balances_list = balance_response["result"]["list"]

        for account in balances_list:
            account_type = account.get("accountType", "N/A")
            total_equity = account.get("totalEquity", "0")
            total_wallet_balance = account.get("totalWalletBalance", "0")
            print(f"\nAccount Type: {account_type}")
            print(f"Total Equity: {total_equity}")
            print(f"Total Wallet Balance: {total_wallet_balance}")

            coins = account.get("coin", [])
            for balance in coins:
                coin = balance["coin"]
                wallet_balance = float(balance.get("walletBalance", 0))
                available_balance = float(balance.get("availableToWithdraw", 0))
                equity = float(balance.get("equity", 0))
                print(f"\nCoin: {coin}")
                print(f"  Wallet Balance: {wallet_balance}")
                print(f"  Available Balance: {available_balance}")
                print(f"  Equity: {equity}")

    except Exception as e:
        print(f"Error fetching balance: {e}")


if __name__ == "__main__":
    main()
