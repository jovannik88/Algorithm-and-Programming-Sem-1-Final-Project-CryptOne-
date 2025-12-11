from Crypto_API import Cryptoapi

def return_to_menu(menu_name="Main Menu"):
    choice = input(f"\nReturn to {menu_name}? (Y/N): ").strip().lower()
    return choice == "y"

def format_history(data):
    if data.get("status") != "success":
        return "Failed to get history data."

    entries = data.get("symbols", [])

    if not entries:
        return "No history found."

    output = "\n========= CRYPTO PRICE HISTORY =========\n"
    output += f"{'Date':<22} {'Close Price (USD)':<15}\n" 
    output += "-" * 40 + "\n"

    #'Date':<22 max character 22 left aligned
    #{'Close Price (USD)':<15}\n"  second column max 15 character

    for entry in entries:
        output += f"{entry['date']:<22} {entry['close']}\n"

    output += "========================================\n"
    return output

def history_menu():
    api = Cryptoapi()

    while True:
        symbol = input("\nEnter crypto symbol for history (ex: BTC, ETH): ").upper()
        
        try:
            limit = int(input("Enter history days(ex: 5, 10, 30): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        print("\nFetching history...\n")

        try:
            data = api.get_history(symbol, limit)
            print(format_history(data))
        except Exception as e:
            print("Error:", e)

        if return_to_menu("Main Menu"):
            break

#Raw Json file
#{'status': 'success', 'symbols': [{'symbol': 'BTC', 'close': '92423.87', 'date': '2025-12-10 23:59:59'}, {'symbol': 'BTC', 'close': '93112.76', 'date': '2025-12-09 23:59:59'}]}
