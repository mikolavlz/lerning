from socket import *

s = socket(AF_INET,SOCK_STREAM) #создали сокет
s.connect(('localhost',8007))
while True:
    msg = input("Введи 1, 2, 3 или q")
    if msg == "1" or msg == "2" or msg == "3" or msg == 'q':
        if msg == 'q':
            break
        else:
            s.send(msg.encode('UTF-8'))
            answer = s.recv(1000000000)
            print(answer.decode('UTF-8'))
    else:
        print('Внимательно следите за тем что вводите')

s.send(msg.encode('UTF-8'))
answer = s.recv(1000000000)
print('Сообщение от сервера: ',answer.decode('UTF-8'))
s.close()