from Car import Car
from random import randint

DEALER_WORK_EXPERIENCE = 10
DISCOUNT = 10


class Factory:
    def __init__(self, title, available_models):
        self.title = title
        self.available_models = available_models
        self.created_cars = []

    # title_car - название авто, которое нужно создать
    # стоимость авто завод устанавливает самостоятельно
    def create_car(self, title_car, age_dealer):
        if not title_car in self.available_models:
            print(f"Завод {self.title} не производит автомобиль {title_car}")
            return

        print(f"Завод {self.title} приступил к изготовлению автомобиля {title_car}.")
        car_price = randint(1000, 5000)
        if age_dealer >= 10:
            print(
                f"В связи со стажем работы дилера от {DEALER_WORK_EXPERIENCE} лет, завод предоставляет скидку в {DISCOUNT}%")
            car_price -= car_price * DISCOUNT / 100
        car = Car(title_car, car_price)
        self.created_cars.append(car)
        return car

    def get_info_amount_created_cars(self):
        title_cars = []
        for created_car in self.created_cars:
            title_cars.append(created_car.title)

        unique_title_cars = set(title_cars)

        print("Продано автомобилей:")
        for unique_title_car in unique_title_cars:
            print(f"{unique_title_car} - {title_cars.count(unique_title_car)} шт.")
