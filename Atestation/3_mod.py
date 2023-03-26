import json
from urllib.request import  urlopen
with urlopen('https://www.cbr-xml-daily.ru/daily_json.js') as response:
    sourse= response.read()
data = json.loads(sourse)
kursdol = int(data["Valute"]["USD"]['Value'])
kurseur = int(data["Valute"]["EUR"]['Value'])

print ('Курс долара = ',kursdol)
print ('Курас евро = ',kurseur)
print('Восколько раз евро больше = ',round ((kurseur/kursdol), 2))