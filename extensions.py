import requests
import json

from contig import exchanges


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def errors_check(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f"Невозможно конвертировать одинаковые валюты в {base}.")

        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise ConvertionException(f"Неправильно введена валюта {quote}.")

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise ConvertionException(f"Неправильно введена валюта {base}.")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Неправильно введено количество {base}.")

        r = requests.get(
            f"https://v6.exchangerate-api.com/v6/a874b74035fac36e3c350227/pair/{base_ticker}/{quote_ticker}/{amount}")

        total_base = json.loads(r.content)['conversion_result']
        return total_base


