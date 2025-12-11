from Crypto_API import Cryptoapi

api = Cryptoapi()


top_count = input("Enter how many Crypto's you want to see (Ex:5,10,20)")

try:
    data = api.get_top_crypto(top_count)
    print(data)

except Exception as e:
    print("Error:", e)

#Raw Json if 3 crypto were selected
#{'status': True, 'symbols': [{'symbol': 'BTC', 'rank': 1, 'last': 90100.21, 'last_btc': 1, 'lowest': 89450.01, 'highest': 92777.3, 'date': '2025-12-11 16:03:11', 'daily_change_percentage': -2.51413406515, 'source_exchange': 'binance'}, {'symbol': 'ETH', 'rank': 2, 'last': 3203.41, 'last_btc': 0.035553857199667, 'lowest': 3171.18, 'highest': 3365.6, 'date': '2025-12-11 16:03:11', 'daily_change_percentage': -4.4622326671697, 'source_exchange': 'binance'}, {'symbol': 'USDT', 'rank': 3, 'last': 1.0001014818449, 'last_btc': None, 'lowest': None, 'highest': None, 'date': '2025-12-11 16:03:12', 'daily_change_percentage': None, 'source_exchange': None}], 'count': 3, 'loaded_time': 0.31425}
