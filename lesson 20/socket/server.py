import time
from socket import *

# AF_INET -указываем что сокет сетевым
# SOCK_STREAM - определяет сокет как потоквый

s = socket(AF_INET,SOCK_STREAM) #создали сокет
s.bind(('',8888))       #настроили сокет по локальному адресу и ипи
s.listen(5) #ожидаем запросы и указываем количество одновременных запросов
while True:
    client,adrr = s.accept()
    print(f'Получен запрос на соединение{str(adrr)}')
    timestr = time.ctime(time.time()) + '\n'
    client.send(timestr.encode('ascii'))
    client.close()
