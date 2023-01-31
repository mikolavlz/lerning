import json
import math
with open('market.json', 'w') as file:
        file.write('''
        {"market": [
    {
      "tovar": "TV",
      "price": "1000"
    },
    {
      "tovar": "PC",
      "price": "2300"
    },
    {
      "tovar": "PS2",
      "price": "10000"
    },
    {
      "tovar": "PS4",
      "price": "2000"
    },
    {
      "tovar": "PSP",
      "price": "500"
    },
    {
      "tovar": "Phone",
      "price": "600"
    }

  ]
}
        ''')
from urllib.request import  urlopen
with urlopen('https://www.cbr-xml-daily.ru/daily_json.js') as response:
    sourse= response.read()
data = json.loads(sourse)
kurs = int(data["Valute"]["USD"]['Value'])
print (kurs)


market_db = "market.json"
data = json.loads(open(market_db).read())
for tovarid in data["market"]:
        price =  int(tovarid['price'])
        tovar = (tovarid['tovar'])
        print(f'Цена товара  {tovar} = {price * kurs} $')