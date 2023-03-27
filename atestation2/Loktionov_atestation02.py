import re
import json
def add_user():
    login_user = input("Введите логин")
    pass_user = (veri_pass())
    with open('user.json', 'r') as file:
        data = json.load(file)
        user_id = {"username": login_user, "pass": pass_user}
        data.append(user_id)
        data_w = json.dumps(data)
    with open('user.json', 'w') as file:
        file.write(data_w)
        file.close()



def print_user():
    data = json.loads(open("user.json").read())
    for userid in data:
        print(f"{userid['username']} {userid['pass']}")

def edit_pass():
    while True :
        in_username = input('Введите имя пользователя')
        data = json.loads(open("user.json").read())
        for userid in data:
            if userid['username'] == in_username:
                print(f"Ваш username {in_username} Ваш пароль {(userid['pass'])}")
                newpass = veri_pass()
                userid['pass'] = newpass
                data_w = json.dumps(data)
                with open('user.json', 'w') as file:
                    file.write(data_w)
                    file.close()
            else:
                print('Пользователь не найден')
        break


def veri_pass():
    pass
    while True:
        passw = input('Введите пароль')
        score = 0
        rules = ["^.{8,}$", "[A-ZА-ЯЁ]+", "[a-zа-яё]+", "\d+", "[!$%&£]+"]
        for x in rules:
            if re.findall(x, passw):
                score += 1
        if score == 5:
            print("Логин и пароль приняты")
            break
        elif score == 3 or score == 4:
            answ = input('Пароль можно сделать лучше \n попробвать еще (y) или оставть как есть (n)')
            if answ == 'n':
                print("Логин и пароль приняты")
                break
        else:
            print('Пароль должен содержать большие и малые буквы а также спец символы(!$%&) и цифры. всего 8 символов')
        break
    return passw








while True:
    inp = input('1 - добавить пользователя\n2 - изменить пароль\n3 - вывести список пользователей\n4 - выход\n')
    if inp == '1':
        add_user()
    elif inp == '2':
        edit_pass()
    elif inp == '3':
        print_user()
    else:
        print('Bye!')
        break





