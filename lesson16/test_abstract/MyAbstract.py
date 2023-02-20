# Абстрактные классы это классы, которые описывают поведение объекта,
# они имеют абстрактные методы, то есть методы, которые могут быть
# пустыми в абстрактном классе и эти методы обязаны быть переопределены
# в классах потомках. Не создавайте объекты абстрактных классов, объекты создавайте
# только у потомков

from abc import ABC,abstractmethod

class MyAbstract(ABC):
    def test(self):
        print("Тестовый неабстрактный метод")
    @abstractmethod
    def my_method1(self):
        pass

    @abstractmethod
    def my_method2(self):
        pass

class MyClass(MyAbstract):
    def my_method1(self):
        print("Метод 1")
        self.test()

    def my_method2(self):
        print("Метод 2")
        self.test()

obj = MyClass()
obj.my_method1()