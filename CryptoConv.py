from Crypto_API import Cryptoapi

def return_to_menu(menu_name="Main Menu"):
    choice = input(f"\nReturn to {menu_name}? (Y/N): ").strip().lower()
    return choice == "y"


def format_currency_data(data, local="USD"):
    if data.get("status") != "success":
        return "Failed to get currency data."

    coin = data["symbols"][0]  # API always returns a list

    # If there is None Values
    last = coin["last"]
    lowest = coin["lowest"] if coin["lowest"] is not None else "N/A"
    highest = coin["highest"] if coin["highest"] is not None else "N/A"

    # Some tokens have no 24h change (USDT, USDC)
    try:
        change = float(coin["daily_change_percentage"])
        change = f"{change:.2f}%"
    except:
        change = "N/A"

    return (
        "\n===== Crypto Currency Data =====\n"
        f"Symbol        : {coin['symbol']}\n"
        f"Last Price    : {last} {local}\n"
        f"Lowest Price  : {lowest} {local}\n"
        f"Highest Price : {highest} {local}\n"
        f"24h Change    : {change}\n"
        f"Last Updated  : {coin['date']}\n"
        "================================\n"
    )


def currency_menu():
    api = Cryptoapi()

    while True:
        symbol = input("Enter crypto symbol (ex: BTC, ETH): ").upper()
        local = input("Enter Currency:  ").upper()
        try:
            data = api.get_data_currency(symbol, local)
            print(format_currency_data(data, local))
        except Exception as e:
            print("Error:", e)
        if return_to_menu("Main Menu"):
            break

#Raw JSON File
#{'status': 'success', 'symbols': [{'symbol': 'BTC', 'last': 1502682704.6399999, 'last_btc': '1', 'lowest': 1491310566.72, 'highest': 1546783145.6000001, 'date': '2025-12-11 15:54:43', 'daily_change_percentage': '-2.4796083522579'}]}
