from random import randint
import math
from factory import Diller


class Order:
    #factory - объект класса Завод
    #models - список названий моделей, которые необходимо изготовить
    #quantity - количество авто в заказе
    def __init__(self, factory, models, quantity):
        self.factory = factory
        self.models = models
        self.quantity = quantity
        self.total_price = 0 #общая стоимость всех созданных авто
        self.cars = []#фура, которую необходимо заполнить готовыми автомобилями
        self.total_vesta = 0
        self.total_niva = 0
        self.tolal_granta = 0
        self.other_car = 0
        # self.start()

    #В данном методе заполним фуру автомобилями
    def start(self,age):
        for i in range(0, self.quantity):
            car = self.factory.create_car(self.models[randint(0, len(self.models) - 1)])
            #проверяю названия моделей на возможность производства и одновременно считаю их количество
            if car.title =="Нива":
                self.total_niva +=1
            elif car.title =="Гранта":
                self.tolal_granta +=1
            elif car.title == "Веста":
                self.total_vesta += 1
            else:
             #если модель не нашли - значит её невозможн опроизвести я считаю количество таких нахзваний
             # и начинаю перебор списка заказаных моделей заново
                print(f"Невозможно произвести {car.title}")
                self.other_car += 1
                continue
            # проверяю возраст дилера - если больше 10 то уменьшаю цену на 10 % и вывожу с точностю до копейки
            if (age > 10):
                car.price = round (car.price * 0.9, 2)
            self.cars.append(car)#погрузили в фуру созданную машину
            self.total_price += car.price

    def show_info(self):
        for i,car in enumerate(self.cars):
            print(f"{i + 1}) Автомобиль {car.title} стоит {car.price}")
        print("Общая стоимость заказа:", self.total_price)
        print(f"всего завод произвел:\nВеста - {self.total_vesta}, Гранта - {self.tolal_granta},\nНива - {self.total_niva}, Невоpможно произвести {self.other_car}")
