# Существует 3 вида методов
# 1. Методы обьекта, то где в первом параметре есть селф . Эти меторды должны запускаться через обьеткы
# обычные методы обьектов
# 2.Обычные функции создавайте как статические методы ю Для создания статического метода
# используйте декоратор @
# 3. Методв класса - это методы которые могут обращаться к свойствам клсаа , онине зависят от обьекта
#
# Статические методы и методв класса вызвваю тпо методу клаасаа а не обьекта .
class Person:
    def __init__(self,fio,age):
        self.fio = fio
        self.age = age

    @staticmethod
    def compare_man(man1,man2):
        if man1.age > man2.age:
            print(f"Сотрудник {man1.age}"
                  f"Старше сотрудника {man2.age} на {man1.age - man2.age} ")
        else:
            print(f"Сотрудник {man2.age}"
                  f" Сnарше сотрудника {man1.age} на {man2.age - man1.age} лет")

person1 = Person("IVAN",30)
person2 = Person("OLEG",35)
# person1.compare_man(person1,person2)
Person.compare_man(person1,person2)