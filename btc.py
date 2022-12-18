import requests


def get_btc_price():
    url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    response = requests.get(url)
    data = response.json()
    return data[0]['price_usd']


btc_price = get_btc_price()
print(f"Le prix actuel du Bitcoin est de : ${btc_price}")
