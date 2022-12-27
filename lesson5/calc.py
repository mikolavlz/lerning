def get_sum(a,b):
    return a + b

def get_raz(a , b):
    return a - b

def get_del(a , b):
    if b == 0:
        print("на ноль делить нельзя")
    return a / b

def get_umn (a , b ):
    return a * b

sign = input("Введите знак")
a = int(input("a = "))
b = int(input("b = "))

def get_resul(sign,a,b):
    if sign == "+":
        get_sum()
    if sign == "-":
        get_raz()
    if sign == "*":
        get_umn()
    get_del()




