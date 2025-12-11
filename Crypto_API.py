import os
import requests
from dotenv import load_dotenv

#Load API Key (API Key are stored in .env File)
load_dotenv()


class Cryptoapi:
    #This is the API that I used for this program
    BASE_URL = "https://api.freecryptoapi.com/v1"

    #Constructor (To Load the API KEY)
    def __init__(self):
        self.api_key = os.getenv("FREECRYPTOAPI_KEY") #"FREECRYPTOAPI_KEY is located in the .env file
        if not self.api_key:
            raise RuntimeError("API Key Error")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    #To Handle the api request (whether it fails/succeed to connect to the API)
    def handle_response(self, endpoint, params):
        response = requests.get(endpoint, params=params, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(
                f"API Error {response.status_code}: {response.text}"
            )

    #Getter Function to get Crypto Data from the API (Used for the 1st menu in the menu page)
    def get_crypto_data(self, symbol):
        endpoint = f"{self.BASE_URL}/getData" #API Link 
        params = {"symbol": symbol} #parameter that are required to fetch the data
        return self.handle_response(endpoint, params)
    
    #Getter Function to convert CryptoCurrency to Real Currency
    def get_data_currency(self, symbol: str, local: str):
        endpoint = f"{self.BASE_URL}/getDataCurrency"
        params = { "symbol": symbol,"local": local}
        return self.handle_response(endpoint, params)
    
    #Getter Function to See The Top Crypto
    def get_top_crypto(self, top):
        endpoint = f"{self.BASE_URL}/getTop"
        params = {"top": top}  
        return self.handle_response(endpoint, params)
    
    #Getter Function to convert From 1 crypto to another Crypto
    def get_conversion(self, from_symbol: str, to_symbol: str, amount: int):
        endpoint = f"{self.BASE_URL}/getConversion"
        params = {"from": from_symbol,"to": to_symbol,"amount": amount}
        return self.handle_response(endpoint, params)
    
    #Getter Function to get history from selected crypto in whatever periods
    def get_history(self,symbol: str,days: int):
            endpoint = f"{self.BASE_URL}/getHistory"
            params = {"symbol": symbol,"days":days}
            return self.handle_response(endpoint, params)
        
# Search Class for menu number 6
class Search:

    #Constructor for searching crypto in Dictionary
    def __init__(self, crypto_dict, currency_dict):
        self.crypto_dict = crypto_dict
        self.currency_dict = currency_dict

    #Function for searching crypto
    def search_symbol(self, dictionary, user_input):
        user_input = user_input.lower()

        #Based on the intital (EX : BTC)
        for symbol, fullname in dictionary.items():
            if user_input == symbol.lower():
                return f"{symbol} → {fullname}"

        #Based on full name
        for symbol, fullname in dictionary.items():
            if user_input == fullname.lower():
                return f"{fullname} → {symbol}"

        #Based on partial fullname
        for symbol, fullname in dictionary.items():
            if user_input in fullname.lower():
                return f"{fullname} → {symbol}"

        #Based on partial symbol
        for symbol in dictionary:
            if user_input in symbol.lower():
                return f"{symbol} → {dictionary[symbol]}"

        return "No matching result found."

    # Search by crypto
    def find_crypto(self, query):
        return self.search_symbol(self.crypto_dict, query)

    # Search by currency
    def find_currency(self, query):
        return self.search_symbol(self.currency_dict, query)

    

