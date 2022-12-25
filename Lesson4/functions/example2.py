
outer = 10
def show_sum(a=1,b=5):
    outer = 2 # внутри функции можно переопределить
    s = a + b + outer
    print(s)
show_sum(1,1)
print(outer) # переменная осталась как была