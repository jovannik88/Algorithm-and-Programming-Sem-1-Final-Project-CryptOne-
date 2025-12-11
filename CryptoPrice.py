from Crypto_API import Cryptoapi

#Def Function to used a choice if wanted to go back to the main menu
def return_to_menu(menu_name="Main Menu"):
    choice = input(f"\nReturn to {menu_name}? (Y/N): ").strip().lower()
    return choice == "y"

def format_crypto_data(data):
    if data.get("status") != "success":
        return "Failed to get data."

    symbol_info = data["symbols"][0]

    formatted = (
        f"\n=== Crypto Information ===\n"
        f"Symbol        : {symbol_info['symbol']}\n"
        f"Last Price    : {symbol_info['last']} USD\n"
        f"Lowest Price  : {symbol_info['lowest']} USD\n"
        f"Highest Price : {symbol_info['highest']} USD\n"
        f"24h Change    : {float(symbol_info['daily_change_percentage']):.2f}%\n"
        f"Source        : {symbol_info['source_exchange']}\n"
        f"Last Updated  : {symbol_info['date']}\n"
        f"==========================\n"
    )
    return formatted

#Function to Run the crypto Price
def crypto_price_menu():
    api = Cryptoapi()

    while True:
        symbol = input("Enter crypto symbol (ex: BTC, ETH, DOGE): ").upper()

        try:
            data = api.get_crypto_data(symbol)
            print(format_crypto_data(data))
        except Exception as e:
            print("Error:", e)

        if return_to_menu("Main Menu"):
            break

#Raw JSON Response{'status': 'success', 'symbols': [{'symbol': 'BTC', 'last': 1531958322.5128, 'last_btc': '1', 'lowest': 1486988257.5452, 'highest': 1540544447.0159998, 'date': '2025-12-08 16:01:20', 'daily_change_percentage': '0.36179294970727'}]}