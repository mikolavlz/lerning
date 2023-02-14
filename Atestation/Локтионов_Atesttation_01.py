print('Програма сичтаеn квадратные кравнения вида a*x^2 + b*x + c = 0')


def is_number(st):
    try:
        float(st)
        return True
    except ValueError:
        return False


err = 1
while err == 1:
    a = input('Введите коэфициент а ')
    b = input('Введите коэфициент b ')
    c = input('Введите коэфициент c ')
    if is_number(a) and is_number(b) and is_number(c):
            break
    print('Нужно вводить числа, пробуй еще')

a = float(a)
b = float(b)
c = float(c)
if a == 0:
        print(f'Уравнение не квадратное х={-c/b}')
if (b**2-4*a*c) < 0:
    print('Уравнение не имеет решения')
else:
    x1 = round(((-b+(b**2-4*a*c))/2*a), 5)
    x2 = round(((-b-(b**2-4*a*c))/2*a), 5)
    if x1==x2:
            print(f'Решение квадратного уравнения x={x1}')
    else:
            print(f'Решение квадратного уравнения x1={x1} x2={x2}')