from Crypto_API import Cryptoapi

api = Cryptoapi()

symbol = input("FROM (ex: BTC, ETH, USD): ").upper()
try:
    data = api.get_crypto_data(symbol)
    print(data)

except Exception as e:
    print("❌ Error:", e)