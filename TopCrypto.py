from Crypto_API import Cryptoapi

def return_to_menu(menu_name="Main Menu"):
    choice = input(f"\nReturn to {menu_name}? (Y/N): ").strip().lower()
    return choice == "y"

def format_top_crypto(data):
    if not data.get("status"):
        return  "Fail to get data."

    output = "\n========== TOP CRYPTOCURRENCIES ==========\n"

    #Loop throught the json file
    for coin in data["symbols"]:
        symbol = coin["symbol"]
        rank = coin.get("rank", "-")

        price = coin["last"]
        change = coin["daily_change_percentage"]

        lowest = coin["lowest"] if coin["lowest"] is not None else "N/A"
        highest = coin["highest"] if coin["highest"] is not None else "N/A"
        change_str = f"{change:.2f}%" if change is not None else "N/A"

        output += (
            f"{rank:>2}. {symbol:<5} | "
            f"Price: {price:<12} | "
            f"24h Change: {change_str:<8} | "
            f"Low: {lowest:<10} | "
            f"High: {highest:<10}\n"
        )

    output += "==========================================\n"
    return output

def top_crypto_menu():
    api = Cryptoapi()

    while True:
        # Ask for top count
        while True:
            try:
                top = int(input("How many top cryptos to display? (ex: 5, 10, 20): "))
                if top > 0:
                    break
                print("Enter a number greater than 0")
            except ValueError:
                print("Please enter a valid number.")

        print("\nLoading Top Cryptocurrencies...\n")

        try:
            data = api.get_top_crypto(top)
            print(format_top_crypto(data))
        except Exception as e:
            print("Error:", e)

        if return_to_menu("Main Menu"):
            break

#json return as dic
#Raw Json Respone
#{'status': True, 'symbols': [{'symbol': 'BTC', 'rank': 1, 'last': 90100.21, 'last_btc': 1, 'lowest': 89450.01, 'highest': 92777.3, 'date': '2025-12-11 16:03:11', 'daily_change_percentage': -2.51413406515, 'source_exchange': 'binance'}, {'symbol': 'ETH', 'rank': 2, 'last': 3203.41, 'last_btc': 0.035553857199667, 'lowest': 3171.18, 'highest': 3365.6, 'date': '2025-12-11 16:03:11', 'daily_change_percentage': -4.4622326671697, 'source_exchange': 'binance'}, {'symbol': 'USDT', 'rank': 3, 'last': 1.0001014818449, 'last_btc': None, 'lowest': None, 'highest': None, 'date': '2025-12-11 16:03:12', 'daily_change_percentage': None, 'source_exchange': None}], 'count': 3, 'loaded_time': 0.31425}