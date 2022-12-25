from random import randint
b = 0
for i in range(1,11):
    a = randint(1,1000)
    print(a)
    b += a
print(f"Среднее = {b / 10}")


