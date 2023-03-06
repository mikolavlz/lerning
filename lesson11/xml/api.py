import json
from urllib.request import  urlopen
valuta = input()
with urlopen('https://www.cbr-xml-daily.ru/daily_json.js') as response:
    sourse= response.read()
data = json.loads(sourse)
print(f'Курс {valuta} сегодня: {format((data["Valute"][valuta]["Value"]))}')