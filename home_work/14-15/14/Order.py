from random import randint

class Order:
    #factory - объект класса Завод
    #models - список названий моделей, которые необходимо изготовить
    #quantity - количество авто в заказе
    def __init__(self,factory,models,quantity):
        self.factory = factory
        self.models = models
        self.quantity = quantity
        self.total_price = 0 #общая стоимость всех созданных авто
        self.cars = []#фура, которую необходимо заполнить готовыми автомобилями

    #В данном методе заполним фуру автомобилями
    def start(self,age):
        for i in range(0,self.quantity):
            car = self.factory.create_car(self.models[randint(0,len(self.models) - 1)])
            self.cars.append(car)#погрузили в фуру созданную машину
            self.total_price += car.price

    def show_info(self):
        for i,car in enumerate(self.cars):
            print(f"{i + 1}) Автомобиль {car.title} стоит {car.price}")
        print("Общая стоимость заказа:",self.total_price)
