import requests
import json
from telebot import types
from config import HEADERS, currencies


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты "{base}".')

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{quote}".')

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{base}".')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}".')

        url = f'https://api.apilayer.com/currency_data/convert?' \
              f'to={quote_ticker}&from={base_ticker}&amount={amount}'
        response = requests.request("GET", url, headers=HEADERS, data={})
        result = json.loads(response.text)["result"]
        result = str(round(result, 2)).replace(".", ",")
        return result


def create_markup(base=None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for c in currencies.keys():
        if c != base:
            buttons.append(types.KeyboardButton(c.capitalize()))

    for b in buttons:
        markup.row(b)

    return markup

amount_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
amount_markup.row(types.KeyboardButton(1))
amount_markup.row(types.KeyboardButton(10))
amount_markup.row(types.KeyboardButton(100))
amount_markup.row(types.KeyboardButton(1000))
amount_markup.row(types.KeyboardButton(10000))

