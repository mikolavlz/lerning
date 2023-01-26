import json
from urllib.request import  urlopen
with urlopen('https://www.cbr-xml-daily.ru/daily_json.js') as response:
    sourse= response.read()
data = json.loads(sourse)
print('kurs dolara:{}'.format((data["Valute"]["USD"])))