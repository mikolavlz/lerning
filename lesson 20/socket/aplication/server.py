import json
from socket import *
from urllib.request import urlopen
def kurs(valuta):
    with urlopen('https://www.cbr-xml-daily.ru/daily_json.js') as response:
        sourse = response.read()
    data = json.loads(sourse)
    return (f'Курс {valuta} сегодня: {format((data["Valute"][valuta]["Value"]))}')

# AF_INET -указываем что сокет сетевым
# SOCK_STREAM - определяет сокет как потоквый

s = socket(AF_INET,SOCK_STREAM) #создали сокет
s.bind(('',8008))       #настроили сокет по локальному адресу и ипи
s.listen(5) #ожидаем запросы и указываем количество одновременных запросов
while True:
    client,adrr = s.accept()
    msg = ("Ты подключился к валютному чат боту\nможешь выбрать какой курс тебе показать\n1.EUR\n2.USD\n3.JPY\nВведи 1, 2, 3 или q")
    client.send(msg.encode('utf-8'))
    data = client.recv(10000000) # получаем данные от клиента
    data1 = data.decode('utf-8')
    if data1 == '1':
        key_valuta = 'EUR'
    elif data1 == '2':
        key_valuta = 'USD'
    elif data1 == '3':
        key_valuta = 'JPY'
    msg = kurs(key_valuta)
    print('Сообщение',data.decode('utf-8'),'было отправленно',adrr)
    client.send(msg.encode('utf-8'))
    client.close()
