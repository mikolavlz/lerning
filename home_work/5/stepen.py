def step(n,s):
    if s == 1:
        return n
    else:
        return n * step(n,s-1)
n = int(input("Введите число "))
s = int(input("Введите положительную степень "))
if s < 0:
    print("Степень должна быть положительной")
else :
    print(f"{n} в степени {s} = {step(n,s)}")