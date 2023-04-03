import json
from re import findall


def create_json_file(dict_users = {}):
    with open("users.json", "w") as file_json:
        json.dump(dict_users,file_json,indent=4)#запишем юзера в файл с учетом форматирования

"""
Данную функцию будем использовать для проверки на дубликат логина
"""
def read_json_file():
    try:
        with open("users.json","r") as file_json:
            return json.load(file_json) #вернем список словарей с юзерами, json.load - преобразует json в список словарей
    except FileNotFoundError:
        return []

"""
lst - список словарей с юзерами, у каждого юзера есть логин и пароль
В этой функции проверяем логин на дубликат
"""
def check_for_dublicate(lst,login):
    for item in lst:
        if item: #если юзер существует, то есть если словарь не пустой
            if item["login"] == login:
                print(f"Логин {login} существует!")
                return True
    return False

def validate_password(password):
    score = 0 #сложность пароля
    rules = ["^.{8,}$","[A-ZА-ЯЁ]+","[a-zа-яё]+","\d+","[!£$%&]+"]
    for x in rules:
        if findall(x,password):
            score += 1
    return score

def is_bad_password(score):
    if 0 <= score <= 2:
        print("Пароль слабый. Введите более надежный пароль")
        return True
    elif 3 <= score <= 4:
        if(input("Пароль можно улучшить! Желаете повторить процедуру (y/n)?") == "y"):
            return True
        else:
            print("Пароль сохранен!")

    return False#значит пароль принят
def write_password():
    while True:
        password = input("Введите пароль")
        if is_bad_password(validate_password(password)):
            continue
        break
    return password


def add_user():
    list_users = read_json_file() #получаем список словарей из файла с юзерами
    while True:
        login = input("Введите логин")
        if check_for_dublicate(list_users,login):
            continue #если логин существует - завершаем итерацию и снова просим ввести логин
        break #если логин уникальный
    password = write_password()
    list_users.append({"login":login,"password":password})
    create_json_file(list_users)


def change_password():
    try:
        list_users = read_json_file()
        if len(list_users) == 0:
            raise Exception("Нет пользователей для изменения пароля")
        while True:
            login = input("Введите логин для которого изменяем пароль")
            if not check_for_dublicate(list_users,login):
                continue #логин не нашли и просим ввести другой
            break
        password = write_password()
        for user in list_users:
            if user['login'] == login:
                user['password'] = password
        print("Пароль успешно изменен")
        create_json_file(list_users)#обновили данные в файле
    except Exception as message:
        print(message)


def print_logins():
    print("Список логинов")
    for user in read_json_file():
        print("\t",user["login"])
    print()


while True:
    try:
        choice = input("Введите номер пункта меню:\n\t "
                       "1 - Добавить пользователя\n\t "
                       "2 - Изменить пароль\n\t "
                       "3 - Вывести список пользователей\n\t "
                       "4 - Выход\n")
        if not choice.isnumeric() or len(choice) != 1:
            raise Exception("Введенное значение не соответствует требованиям")
        elif choice == "1":
            add_user()
        elif choice == "2":
            change_password()
        elif choice == "3":
            print_logins()
        elif choice == "4":
            break
    except Exception as message:
        print(message)#в случае ошибки выведем сообщение, указанное в raise
        print()
        continue