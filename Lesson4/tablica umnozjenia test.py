from random import randint
count_error = 0
for i  in range (0,5):
    a = randint(1,10)
    b = randint(1,10)
    corect = a * b
    answer = int(input(f"{a} * {b} = "))
    if answer != corect:
        count_error += 1
if count_error == 0:
    print("Оценка 5")
if count_error == 1:
    print("Оценка 4")
if count_error == 2:
    print("Оценка 3")
if count_error == 3:
    print("Оценка 2")
elif count_error == 4:
    print("Оценка 1")
elif count_error == 5:
    print("незачет")
