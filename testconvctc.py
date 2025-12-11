from Crypto_API import Cryptoapi

api = Cryptoapi()


from_symbol = input("Convert FROM (ex: BTC, ETH): ").upper()
to_symbol = input("Convert TO (ex: ETH, BTC): ").upper()

amount = float(input("Amount: "))

try:
    data = api.get_conversion(from_symbol, to_symbol, amount)
    print(data)

except Exception as e:
    print("Error:", e)

#Raw Json File
#{'status': 'success', 'result': 28.14347687480075}
