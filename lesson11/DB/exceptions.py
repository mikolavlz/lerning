from random import randint
num1 = 10
num2 = randint(0,2)


# для обработки ошиби try И except
# в блоке try инструкции кторые приводят к ошибке  ипередаеться
# в блокк except
# try:
#     print(num1/num2)
# except ZeroDivisionError:
#     print('делениена ноль')
# print('строка')

while True:
    first_num = input("первое число")
    if first_num == 'q':
        break
    second_num = input("второе число")
    if first_num == 'q':
        break
    try:
        res = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print('делениена ноль')
    else:
        print("частное  = ", res)