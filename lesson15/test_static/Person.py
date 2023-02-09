class Person:
    def __init__(self,fio,age):
        self.fio = fio
        self.age = age

    def compare_man(self,man1,man2):
        if man1.age > man2.age:
            print(f"Сотрудник {man1.age}"
                  f"Старше сотрудника {man2.age} на {man1.age - man2.age}")
        else:
            print(f"Сотрудник {man2.age}"
                  f"ТСарше сотрудника {man1.age} на {man2.age - man1.age}")

person1 = Person("IVAN",30)
person2 = Person("OLEG",35)
person1.compare_man(person1,person2)