rez_sum = lambda a,b : a+b
rez_raz = lambda a,b : a-b
rez_umn = lambda a,b : a*b
rez_del = lambda a,b : a/b

def get_resul(sign,a,b):
    if sign == "+":
        print(rez_sum(a,b))
    if sign == "-":
        print(rez_raz(a,b))
    if sign == "*":
        print(rez_umn(a,b))
    if sign == "/":
        if b == 0:
            print("На ноль делить нельзя")
        else:
            print (rez_del(a,b))


sign = input("Введите знак ")
if sign == "+" or sign == "-" or sign == "*" or sign == "/":
    a = int(input("a = "))
    b = int(input("b = "))
    get_resul(sign, a, b)
else:
    print("Такого действия не существует")



