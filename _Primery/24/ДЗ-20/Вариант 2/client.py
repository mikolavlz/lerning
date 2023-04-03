import socket

# создадим объект сокета
client_socket = socket.socket()

# получим локальное имя
host = socket.gethostname()
port = 5555

# подключимся к нашему серверу
client_socket.connect((host, port))

# получить приветственное сообщение от сервера
message = client_socket.recv(10000).decode("utf-8")
print(message)

# цикл для отправки и получения сообщений с сервером
while True:
    # получить сообщение от пользователя
    message = input("Вы: ")

    # отправить сообщение на сервер
    client_socket.send(bytes(message, "utf-8"))

    # получить ответ от сервера
    response = client_socket.recv(10000).decode("utf-8")

    # распечатать ответ от сервера
    print("Bot:", response)

    # прервать цикл, если пользователь хочет выйти
    if message.lower() == "пока":
        client_socket.close()
        break
