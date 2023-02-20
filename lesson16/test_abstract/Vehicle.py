from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,title):
        self.title = title

    def show_info(self):
        print("Информация о транспортном средстве:",self.number_wheels())

    @abstractmethod
    def number_wheels(self):
        pass

class Car(Vehicle):
    def __init__(self, title):
        super().__init__(title)

    def number_wheels(self):
        return f"Автомобиль {self.title} имеет от 4 колес"

class Bike(Vehicle):
    def __init__(self, title):
        super().__init__(title)
    def number_wheels(self):
       return f"Мотоцикл {self.title} имеет от 2-3 колес"


bike = Bike("Урал")
bike.show_info()