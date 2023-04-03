from socket import *



s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',8888))
msg = input('Введите 1, если хотите узнать время\n'
            '2 - курс доллара\n'
            '3 - операции с числами\n'
            '4 - дату\n'
            '5 - рассказать анекдот\n')
s.send(msg.encode('UTF-8'))

n = msg
if n == '1':
    tm = s.recv(1024)#принимать не более 1024 байт
    print(f"Текущее время: {tm.decode('ascii')}")
elif n == '2':
     answer = s.recv(1000000000)
     print('Сообщение от сервера: ', answer.decode('UTF-8'), 'руб.')
elif n == '3':
    msg1 = input('Введите первое число пробел знак операции пробел и второе число\n')
    s.send(msg1.encode('UTF-8'))
    answer = s.recv(1000000000)
    print('Сообщение от сервера: ', answer.decode('UTF-8'))
elif n == '4':
    td = s.recv(1024)  # принимать не более 1024 байт
    print(f"Текущая дата: {td.decode('ascii')}")
elif n == '5':
    answer = s.recv(1000000000)
    print('Сообщение от сервера: ', answer.decode('UTF-8'))


s.close()
