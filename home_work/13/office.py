class Office:
    # В конструкторе описываются поля класса(свойства объекта)
    # Поля класса доступны в любом нестатическом методе, то есть в любом, где
    # первый параметр self. Из методов обращаемся к полям класса через self

    def __init__(self,title,persons):
        self.title = title
        self.persons = persons

    def show_info(self):
        print(f"Название офиса: {self.title}\nВ офисе работают следующие сотрудники:")
        i = 1
        for man in self.persons:
            print(f"{i}){man.get_info()}")
            i += 1
        man_max = self.get_man_max_salary()
        man_min = self.get_man_min_salary()
        print(f"Сотрудник {man_max.fio} имеет максимальный оклад {man_max.salary}")
        print(f"Сотрудник {man_min.fio} имеет максимальный оклад {man_min.salary}")
    # Получаем сотрудника с макс. окладом
    def get_man_max_salary(self):
        # Пусть первый сотрудник имеет макс. оклад
        man_max = self.persons[0]
        for i in range(1,len(self.persons)):#обошли всех сотрудников, начиная со 2го и сравнили каждого с первым по свойству оклад
            if self.persons[i].salary > man_max.salary:
                man_max = self.persons[i]
        return man_max #методу присвоили сотрудника с макс. окладом

    def get_man_min_salary(self):
        # Пусть первый сотрудник имеет мин. оклад
        man_min = self.persons[0]
        for i in range(1,len(self.persons)):#обошли всех сотрудников, начиная со 2го и сравнили каждого с первым по свойству оклад
            if self.persons[i].salary < man_min.salary:
                man_min = self.persons[i]
        return man_min #методу присвоили сотрудника с мин. окладом

class Person:
    # self - это ссылка на объект, который мы заполняем свойствами после его создания
    # Цель функции конструктора - заполнить объект свойствами и его вернуть. Поэтому
    # в конструкторе никогда нет оператора return, потому что конструктор всегда возвращает
    # объект нашего класса
    def __init__(self,fio,age,salary):#self означает, что в этом методе работаем с объектом данного класса, то есть метод относится к объекту
        self.fio = fio #self - это объект, который запускает конструктор
        self.age = age
        self.salary = salary

    def get_info(self):#self ссылается на объект, который вызывает наш метод
        return f"Сотрудник {self.fio} имеет оклад {self.salary}, возраст: {self.age}"


# Создали объект, заполнили его свойствами и каждому свойству присвоили значение.
# Всегда при создании объекта вызывается функция конструктор
man1 = Person("Иванов",30,70000)
man2 = Person("Петров",36,90000)
man3 = Person("Сидоров",32,80000)

men = [man1,man2,man3]


company = Office("IT Start",men)
company.show_info() #выведем всю информацию об офисе
