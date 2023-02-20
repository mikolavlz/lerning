# Создайте абстрактный класс, который определяет базовую ставку зарплаты для сотрудников фирмы. Создайте подклассы данного класса для детализации заработной платы для различных видов сотрудников. Пусть зарплата программиста составляет 4 базовых ставки, а зарплата экономиста – две базовых ставки, а коэффициент зарплаты директора равен 10.

from abc import ABC,abstractmethod

class Person(ABC):
    base_rate = 30000
    # position = ""
    def __init__(self,position):
        self.position = position

    @abstractmethod
    def get_koefficient(self):
        pass

    def calc_salary(self):
        salary = self.base_rate * self.get_koefficient()
        print("Сотрудник в дожлности ",self.position,"зарабатывает",salary)