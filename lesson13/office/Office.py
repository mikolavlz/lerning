class Person:
    # self -ссылка на обьект , который мы заполняем свойствами после зоздания
    # цель функции конструктора запонить обьект свойствами и его вернуть .

     def __init__(self,fio,age,salary): #self означает что работаем с обьектом
        self.fio = fio
        self.age = age
        self.salary = salary

 # создали обьект и заполнили его свойствами и значениями
man1 = Person('Иванов',30,70000)
man2 = Person('Petov',60,80000)
man3 = Person('Sidorov',46,87000)
oficce = [man1,man2,man3]
for man in oficce:
 print(f'сотрудник {man.fio} имеет оклад {man.salary}')

