import socket
import datetime
import locale

# создадим объект сокета
server_socket = socket.socket()

# получим локальное имя
host = socket.gethostname()
port = 5555

#настроили сокет, чтобы он принимал запросы от клиента по локальному IP и порту
server_socket.bind((host, port))

# настройка количества клиентов, которых сервер может прослушивать одновременно - 5
server_socket.listen(5)

# функция для получения текущего времени
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S") #используем метод модуля datetime для получения
    # времени в виде строки заданного формата
    return current_time

# функция для получения текущей даты
def get_date():
    now = datetime.datetime.now()
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8') #для того чтобы получить дату на Русском
    day = now.strftime('%A')
    return f"Сегодня {day}, {now.strftime('%d %B %Y')} года"

# функция для выполнения простых арифметических операций
def calculate(operation):
    result = eval(operation) #eval() - это встроенная функция Python, которая принимает строку на вход и
                             #оценивает (выполняет) ее как выражение или оператор Python.
    return result

while True:
    # устанавливаем связь с клиентом
    client_socket, addr = server_socket.accept()

    print(f"Установлено соединение с {addr}")

    # отправим приветствие клиенту
    client_socket.send(bytes("Добро пожаловать в чат-бот! Чем я могу помочь вам сегодня?", "utf-8"))

    # цикл для получения и отправки сообщений с клиентом
    while True:
        # получить сообщение от клиента
        message = client_socket.recv(10000).decode("utf-8")

        # прервем цикл если сообщение пустое (клиент отсоединился)
        if not message:
            break
        # проверять наличие различных типов вопросов и давать соответствующие ответы
        if message.lower() == "который час?":
            response = get_time()
        elif message.lower() == "какой сегодня день?":
            response = get_date()
        elif "калькулятор" in message.lower():
            operation = message.split("калькулятор")[1].strip()
            try:
                response = str(calculate(operation)) #Перевожу полученное значение в строковый тип, иначе возникнет
                # Ошибка "У объекта int нет атрибута 'encode'" когда вызываем метод encode() на объекте integer.
            except ZeroDivisionError:
                response = "Каждый знает, что на ноль делить нельзя"
            except:
                response = "Извините, я не смог выполнить эту операцию. Пожалуйста, попробуйте еще раз."
        elif message.lower() == "привет":
            response = "Здравствуйте! Чем я могу помочь вам сегодня?"
        elif message.lower() == "пока":
            response = "До встречи! Хорошего дня!"
            client_socket.send(bytes(response, "utf-8"))
            client_socket.close()
            break
        else:
            response = "Извините, я не понял ваш вопрос. Пожалуйста, попробуйте еще раз."

        # отправить ответ клиенту
        client_socket.send(bytes(response, "utf-8"))
