from factory.Car import Car
from random import randint


class Factory:
    def __init__(self,title):
        self.title = title

    #title_car - название авто, которое нужно создать
    #стоимость авто завод устанавливает самостоятельно
    def create_car(self,title_car):
        print(f"Завод {self.title} приступил к изготовлению автомобиля {title_car}")
        car = Car(title_car,randint(1000,5000))
        return car