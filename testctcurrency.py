from Crypto_API import Cryptoapi

api = Cryptoapi()

symbol = input("FROM (ex: BTC, ETH, USD): ").upper()
local =  input("Enter Currency")
try:
    data = api.get_data_currency(symbol,local)
    print(data)

except Exception as e:
    print("Error:", e)

# Raw JSon
#{'status': 'success', 'symbols': [{'symbol': 'BTC', 'last': 1502682704.6399999, 'last_btc': '1', 'lowest': 1491310566.72, 'highest': 1546783145.6000001, 'date': '2025-12-11 15:54:43', 'daily_change_percentage': '-2.4796083522579'}]}