from Crypto_API import Cryptoapi

def return_to_menu(menu_name="Main Menu"):
    choice = input(f"\nReturn to {menu_name}? (Y/N): ").strip().lower()
    return choice == "y"

def format_conversion(data, from_symbol, to_symbol, amount):
    if data.get("status") != "success":
        return "Conversion failed."

    result = data.get("result")

    return (
        "\n========== CONVERSION RESULT ==========\n"
        f"From       : {amount} {from_symbol}\n"
        f"To         : {to_symbol}\n"
        f"Converted  : {result}\n"
        "=======================================\n"
    )

def conversion_menu():
    api = Cryptoapi()

    while True:

        from_symbol = input("Input the crypto that you want to convert (ex: BTC, ETH, Doge): ").upper()
        to_symbol = input("Input the crypto you want to convert  (ex: BTC, ETH, Doge): ").upper()

        try:
            amount = float(input("Amount to convert: "))
        except ValueError:
            print("Enter a valid number for amount.")
            continue

        print("\nConverting...\n")

        try:
            data = api.get_conversion(from_symbol, to_symbol, amount)
            print(format_conversion(data, from_symbol, to_symbol, amount))
        except Exception as e:
            print("Error:", e)

        if return_to_menu("Main Menu"):
            break

#Raw Json File
#{'status': 'success', 'result': 28.14347687480075}
