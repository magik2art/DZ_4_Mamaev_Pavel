import datetime
import requests
from bs4 import BeautifulSoup


def currency_rates(id_):
    global dollar
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    value = str(soup.find("valcurs"))
    value_index = value.find(id_)
    value_info = value[(value_index - 61):(value_index + 79)]
    id_index1 = value_info.find('id=')
    id_index = (value_info[(id_index1 + 4):id_index1 + 11])
    if value.find(id_) == -1:
        print(None)
    else:
        if id_index[-1] == '"':
            id_index = id_index[0:6]
        else:
            print()
        valute_id_info = str(soup.find_all(id=id_index))
        price_index = valute_id_info.find("value")
        x = (valute_id_info[(price_index + 6):(price_index + 13)])
        x = x.split(",")
        dullar = x[0]
        dollar = x[0]
        cent = x[1]
        if float(cent) < 999:
            cent = float(cent) / 1000
        else:
            cent = float(cent) / 10000
        price = "{0:.2f}".format(float(dollar) + float(cent))
        return float(price)


def currency_rates_name(id, name):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    value = str(soup.find("valcurs"))
    value_index = value.find(id)
    value_info = value[(value_index - 61):(value_index + 79)]
    name_index_start = value_info.find("name")
    name_index_end = value_info.find("/name")
    name = value_info[(name_index_start + 5):(name_index_end - 1)]
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


# Использовал для тестового прогона

# code_list = [["AUD"], ["AZN"], ["GBP"], ["AMD"], ["BYN"], ["BGN"], ["BRL"], ["HUF"], ["HKD"], ["DKK"]
#              , ["USD"], ["EUR"], ["INR"], ["KZT"], ["CAD"], ["KGS"], ["CNY"], ["MDL"], ["NOK"], ["PLN"], ["PL1"]]
# print(code_list[0][0])
# i = 0
# while i < len(code_list):
#     code = code_list[i][0]
#     i += 1
#     price = currency_rates(code)
#     name = "Valute"
#     Valute_name = currency_rates_name(code, name)
#     print("Стоимость 1 единицы валюты (" + Valute_name + ") = ", price, "рублей за 1 единицу")
#     Date = currency_rates_date(code, name)
#     print("Данные актуальны на дату: ", Date)

code = input("Введите транскрипцию валюты(к примеру доллар - USD, а ЕВРО - EUR): ")
code = code.upper()
price = currency_rates(code)
name = "Valute"
Valute_name = currency_rates_name(code, name)
print("Стоимость 1 единицы валюты (" + Valute_name + ") = ", price, "рублей за 1 единицу")
Date = currency_rates_date(code, name)
print("Данные актуальны на дату: ", Date)
