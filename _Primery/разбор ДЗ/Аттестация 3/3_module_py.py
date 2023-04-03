import json
from urllib.request import urlopen

with urlopen("https://www.cbr-xml-daily.ru/daily_json.js") as response:
    sourse = response.read()
data = json.loads(sourse)

usd = data['Valute']['USD']['Value']
euro = data['Valute']['EUR']['Value']

print("Курс доллара: {}".format(usd))
print("Курс евро: {}".format(euro))
print("Курс доллара отличается от курса евро в: {} раз".format(usd/euro))
