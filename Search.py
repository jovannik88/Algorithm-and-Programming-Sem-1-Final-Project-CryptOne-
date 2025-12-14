from CryptoList import CRYPTO_TOKENS, CURRENCY_LIST
from Crypto_API import Search

def return_to_menu(menu_name="Main Menu"):
    choice = input(f"\nReturn to {menu_name}? (Y/N): ").strip().lower()
    return choice == "y"

def run_search_cli():
    searcher = Search(CRYPTO_TOKENS, CURRENCY_LIST)
    while True:
        user_input = input("\nEnter crypto/currency name or symbol: ").strip()

        # Try crypto search first
        result_crypto = searcher.find_crypto(user_input)
        if "no result"not in result_crypto:
            print("Crypto:", result_crypto)
        else:
            # Try currency if not found in crypto
            result_currency = searcher.find_currency(user_input)
            if "no result" not in result_currency:
                print("Currency:", result_currency)
            else:
                print("No matching crypto or currency found.")

        
        if return_to_menu("Search Menu"):
            print("\nExiting Search...")
            break


if __name__ == "__main__":
    run_search_cli()

