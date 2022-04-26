import requests
import json
from  config import  keys

class conversionException(Exception):
    pass

class cryptoconverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise conversionException(f'нельзя конвертировать одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise conversionException(f'не удалось обработать валюту {quote}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise conversionException(f'не удалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise conversionException(f'не удалось обработать коичество {amount}.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base