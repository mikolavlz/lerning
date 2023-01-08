def get_sum(a,b):
    print(int(a+b))
def get_raz(a,b):
    print(int(a-b))
def get_del(a,b):
    if b == 0:
        print("на ноль делить нельзя")
    else:
        print(int(a/b))
def get_umn (a,b ):
    print(int(a*b))
def get_resul(sign,a,b):
    if sign == "+":
        get_sum(a,b)
    if sign == "-":
        get_raz(a,b)
    if sign == "*":
        get_umn(a,b)
    if sign == "/":
        get_del(a,b)

sign = input("Введите знак ")
a = int(input("a = "))
b = int(input("b = "))
get_resul(sign,a,b)


