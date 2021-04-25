import argparse
import currency


parser = argparse.ArgumentParser(description='Return cost of Valutue. Input string:')
parser.add_argument('indir', type=str, help='Введите транскрипцию валюты(к примеру доллар - USD, а ЕВРО - EUR): ')
args = parser.parse_args()
code = args.indir
code = code.upper()
price = currency.currency_rates(code)
name = "Valute"
Valute_name = currency.currency_rates_name(code, name)
print("Стоимость 1 единицы валюты (" + Valute_name + ") = ", price, "рублей за 1 единицу")
Date = currency.currency_rates_date(code, name)
print("Данные актуальны на дату: ", Date)
