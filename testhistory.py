from Crypto_API import Cryptoapi

api = Cryptoapi()

# === TEST VALUES ===
symbol = input("FROM (ex: BTC, ETH, USD): ").upper()
days = int(input("Enter how many days: "))

try:
    data = api.get_history(symbol,days)
    print(data)

except Exception as e:
    print("Error:", e)

#Raw Json file
#{'status': 'success', 'symbols': [{'symbol': 'BTC', 'close': '92423.87', 'date': '2025-12-10 23:59:59'}, {'symbol': 'BTC', 'close': '93112.76', 'date': '2025-12-09 23:59:59'}]}