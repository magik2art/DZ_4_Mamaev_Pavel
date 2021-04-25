import datetime
import requests
from bs4 import BeautifulSoup


def currency_rates(id):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    value = soup.find(id=id)
    value = value.find("value")
    price = str(value)
    dollar = float(price[7:(len(price)-13)])
    cent = float(price[10:(len(price)-10)])
    cent = float(cent) / 100
    price = dollar + cent
    return float(price)


def currency_rates_name(id, name):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    value = soup.find(id=id)
    name = value.find("name")
    name = str(name)
    name = name[6:(len(name)-7)]
    Valute = name
    return Valute


def currency_rates_date(id, date):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    value = soup.find(date="")
    date = str(value.valcurs)
    date = date[15:25]
    date = datetime.date(int(date[6:10]), int(date[3:5]), int(date[0:2]))
    return date

# code = input("Введите id валюты(к примеру доллар - R01235, а ЕВРО - R01239): ")
code = "R01239"
price = currency_rates(code)
name = "Valute"
Valute_name = currency_rates_name(code, name)
print("Стоимость 1 единицы валюты (" + Valute_name + ") = ", price, "рублей за 1 единицу")


code = "R01235"
price = currency_rates(code)
name = "Valute"
Valute_name = currency_rates_name(code, name)
print("Стоимость 1 единицы валюты (" + Valute_name + ") = ", price, "рублей за 1 единицу")

Date = currency_rates_date(code, name)
print("Данные актуальны на дату: ", Date)
