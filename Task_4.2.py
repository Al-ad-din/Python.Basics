print('Задание № 2')

from requests import get, utils
import decimal

def currency_rates(char_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    currency_dict = {}
    for n in content.split('</Value>'):
        i = n.split('</CharCode>')[0][-3:]
        currency_dict[i] = n[-7:] if i.isalpha() else print()

    char_code = char_code.upper()
    if currency_dict.setdefault(char_code) == None:
        print('Код валюты не найден')
    else:
        price = decimal.Decimal(currency_dict[char_code].replace(',', '.')).quantize(decimal.Decimal('0.01'))
        print(f'{char_code} = {price} руб.')

currency_rates(input('Введите код валюты: '))
