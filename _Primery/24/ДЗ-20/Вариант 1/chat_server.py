
from socket import *
import time

from datetime import date

import requests


from random import randint

s = socket(AF_INET,SOCK_STREAM) #создали сокет TCP
s.bind(("",8888)) #настроили сокет, чтобы он принимал запросы от клиента по локальному IP и порту
s.listen(5)#Переходим в режим ожидания запросов и допускаем не более 5 запросов одновременно
while True:
    client,addr = s.accept()#принимаем запрос на соединение
    print(f"Получен запрос на соединение {str(addr)}")

    data = client.recv(10000000)  # получаем данные от клиента
    n = data.decode('UTF-8')

    if n == '1':
        timestr = time.ctime(time.time()) + "\n"
        client.send(timestr.encode('ascii'))
    elif n == '2':
        rate_usd = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        rate_usd_rrf = rate_usd['Valute']['USD']['Value']
        msg = (f'Курс доллара {rate_usd_rrf}')
        client.send(msg.encode('UTF-8'))


    elif n == '3':
        data = client.recv(10000000)  # получаем данные от клиента
        data1 = data.decode('UTF-8')

        data2 = data1.split(' ')
        num1 = float(data2[0])
        num2 = float(data2[2])
        z = data2[1]
        if z == '+':
            rez = num1 + num2
        elif z == '-':
            rez = num1 - num2
        elif z == '*':
            rez = num1 * num2
        elif z == '/':
            if num2 != 0:
                rez = num1 / num2
        msg = (f'Результат = {rez}')

        client.send(msg.encode('UTF-8'))

    elif n == '4':
        current_date = date.today()
        current_date_string = current_date.strftime('%d-%b-%Y')
        client.send(current_date_string.encode('UTF-8'))
    elif n == '5':
        y = randint(1, 3)
        if y == 1:
            msg = 'Важна не длина пароля, а умение им пользоваться!'
        elif y == 2:
            msg = 'Гелендваген — это правильно собранный уазик.'
        elif y == 3:
            msg = 'Чтобы добро победило зло, его надо сначала разозлить.'
        client.send(msg.encode('UTF-8'))

    client.close()



