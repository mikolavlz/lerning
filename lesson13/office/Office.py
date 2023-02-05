class office:
    def __init__(self,title,persons):
        self.title = title
        self.person = persons
    def show_info(self):
        print(f'Название офиса{self.title}\n В офисе рабоатею следующие сотрудники\n')
        i=1
        for man in self.person:
            print(f'{i}{man.get_info}')
            i +=1
    def get_man_max_salary(self):
        man_max = self.person[0]
        for i in range (1, self.person):
            if self.person[i].salary > man_max.salary:



class person:
    # self -ссылка на обьект , который мы заполняем свойствами после зоздания
    # цель функции конструктора запонить обьект свойствами и его вернуть .

    def __init__(self,fio,age,salary): #self означает что работаем с обьектом
        self.fio = fio
        self.age = age
        self.salary = salary
    def get_info(self):
        return (f'сотрудник {self.fio} имеет оклад {self.salary}')


 # создали обьект и заполнили его свойствами и значениями
man1 = person('Иванов',30,70000)
man2 = person('Petov',60,80000)
man3 = person('Sidorov',46,87000)
oficce = [man1,man2,man3]
for man in oficce:
 print(man.get_info())
men = [man1,man2,man3]
company = ofice.