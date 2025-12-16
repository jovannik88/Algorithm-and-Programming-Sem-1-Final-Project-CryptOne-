# Import the Function from each specific files (def function)
from CryptoPrice import crypto_price_menu
from CryptoConv import currency_menu
from TopCrypto import top_crypto_menu
from convcrytocry import conversion_menu
from history import history_menu
from Search import run_search_cli

#Printing the menu, and 
def show_menu(options):
    print("=== Welcome TO MyCryptOne ===")
    print("=== All In One Crypto Solution ===")

    for index, option in enumerate(options, start=1): #Enumarate= loop throught list and get index automatic
        print(f"{index}. {option}")

    print("0. Exit")


#Get user Choice
def get_choice(max_choice):
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if 0 <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a number between 0 and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Main Menu
def main():
    options = [
        "Crypto Price",
        "Crypto Converter (EX : BTC to IDR)",
        "Top Crypto List","Crypto Converter(EX : BTC to ETH)","Crypto History","Search"
    ] #list
    
    while True:
        show_menu(options)
        choice = get_choice(len(options))

        if choice == 0:
            print("Exiting program...")
            break

        print(f"You selected: {options[choice - 1]}")

        if choice == 1:
            crypto_price_menu() 
        if choice ==2:
            currency_menu()
        if choice ==3:
            top_crypto_menu()
        if choice ==4:
            conversion_menu()
        if choice ==5:
            history_menu()
        if choice ==6:
            run_search_cli()

if __name__ == "__main__":
    main()
