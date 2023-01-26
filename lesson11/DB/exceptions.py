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

# while True:
#     first_num = input("первое число")
#     if first_num == 'q':
#         break
#     second_num = input("второе число")
#     if first_num == 'q':
#         break
#     try:
#         res = int(first_num)/int(second_num)
#     except ZeroDivisionError:
#         print('делениена ноль')
#     else:
#         print("частное  = ", res)

# try:
#     x = int(input("thislo"))
#     res = 10 / x
#
#     print(res)
# except ZeroDivisionError:
#     print("на ноль")
# except ValueError:
#     print("некоректное значение")
# except:
#     print("error")

# пример 3. расшифровка ошибок
#
# try:
#     x = int(input("thislo"))
#     res = 10 / x
#     print(res)
# except ZeroDivisionError as test:
#     print("на ноль {}".format(test))
# except ValueError as test2:
#     print("некоректное значение {}".format(test2))
# except:
#     print("error")

# #4 пример
# my_file = 'test.txt'
# try:
#     with open(my_file,encoding="utf-8") as file:
#         content = file.readlines()
# except FileNotFoundError:
#     print("Фаил не найден")
#
#

# 5пример
# try:
#     num = int(input("введите число"))
#     assert num % 2 == 0
# except:
#     print("Число не четное")
# else:
#     print(1 / num)

# после try можно вместо except испольовать finally -инструкции выполняються обчзательно
# try:
#     file = open('test.txt')
#     content = file.readlines()
# finally:
#     file.close()

# генерация исключений

# если мы хотим напугать пользователя ошибкой используем raise
try:
    age = int(input("введи возраст от 20 -25"))
    if 20 <= age <= 25:
        print('ok')
    else:
        raise ValueError('Вы ввели неправильный возраст')
except Exception as e:
    # print(f"Возникла ошибка{e}")
    print(e)
print(111)