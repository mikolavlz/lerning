from socket import *

s = socket(AF_INET,SOCK_STREAM) #создали сокет
s.connect(('localhost',8008))
answer = s.recv(1000000000)
print(answer.decode('UTF-8'))
while True:
    msg = input("цифра ? ")
    if msg == "1" or msg == "2" or msg == "3" or msg == 'q':
        if msg == 'q':
            break
        else:
            s.send(msg.encode('UTF-8'))
            print("s.send(msg.encode('UTF-8'))")
            answer = s.recv(1000000000)
            print("answer = s.recv(1000000000)")

            print(answer.decode('UTF-8'))
    else:
        print('Внимательно следите за тем что вводиш')
s.close()