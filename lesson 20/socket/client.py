from socket import *

s = socket(AF_INET,SOCK_STREAM) #создали сокет
s.connect(('localhost',8888))
tm = s.recv(1024) #принимать не более 1024 бт
s.close()
print(f'Текущее время :{tm.decode("ascii")}')