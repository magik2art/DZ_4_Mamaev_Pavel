import datetime
import requests
from bs4 import BeautifulSoup


def currency_rates(id):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    value = str(soup.find("valcurs"))
    value_index = value.find("USD")
    value_info = value[(value_index - 61):(value_index + 79)]
    price_index = value_info.find("value")
    price = str(value_info[(price_index + 6):(price_index + 8)])
    dollar = float(value_info[(price_index + 6):(price_index + 8)])
    cent = float(value_info[(price_index + 9):(price_index + 11)])
    cent = float(cent) / 100
    price = dollar + cent
    print(price)
    return float(price)

code = "R01239"
price = currency_rates(code)
name = "Valute"
print("Стоимость 1 единицы валюты (" ") = ", price, "рублей за 1 единицу")

