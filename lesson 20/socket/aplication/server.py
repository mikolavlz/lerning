
from socket import *

# AF_INET -указываем что сокет сетевым
# SOCK_STREAM - определяет сокет как потоквый

s = socket(AF_INET,SOCK_STREAM) #создали сокет
s.bind(('',8007))       #настроили сокет по локальному адресу и ипи
s.listen(5) #ожидаем запросы и указываем количество одновременных запросов
while True:
    client,adrr = s.accept()
    msg = ("Ты подключился к чат боту\nты можешь выбрать что тебе показать\n1.Погоду\n2.Курс долара\n3.Время")
    client.send(msg.encode('utf-8'))
    data = client.recv(10000000) # получаем данные от клиента
    data1 = data.decode('utf-8')
    data3 = data1.split(' ')
    temp = int(data3[0])+int(data3[1])
    msg = (f'Сумма = {temp}')
    print('Сообщение',data.decode('utf-8'),'было отправленно',adrr)
    client.send(msg.encode('utf-8'))
    client.close()
