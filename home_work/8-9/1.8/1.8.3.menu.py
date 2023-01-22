import random
def random_1():
    a = random.randrange(5,20,1)
    b = random.randrange(5, 20, 1)
    sum_user=int(input(f' {a}+{b} = ? '))
    print(f'{a} + {b} = {a + b}\nВаш ответ = {sum_user} ')
    proverka(sum_user, a + b)
def random_2():
    a = random.randrange(25, 50, 1)
    b = random.randrange(1, 25, 1)
    raz_user = int(input(f' {a}-{b} = ? '))
    print(f'{a} - {b} = {a - b}\nВаш ответ = {raz_user} ')
    proverka(raz_user,a-b)
def proverka(user_var,pc_var):
    if user_var == pc_var:
        print("Верно")
    else:
        print(f"Неверно, правилньный ответ = {pc_var}")
trig = 1
while trig == 1:
    key = input("введите 1 для сложения или 2 для вычитания ")
    if key == '1':
       random_1()
       trig = 0
    elif key == '2':
        random_2()
        trig = 0



