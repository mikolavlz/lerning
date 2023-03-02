from socket import *

s = socket(AF_INET,SOCK_STREAM) #создали сокет
s.connect(('localhost',8007))
msg = '2 6'
s.send(msg.encode('UTF-8'))
answer = s.recv(1000000000)
print('Сообщение от сервера: ',answer.decode('UTF-8'))
s.close()