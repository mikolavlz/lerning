from random import randint

from Diller import Dealer
from Factory import Factory
from Order import Order

available_models_factory = ["Веста", "Гранта", "Нива"]
factory = Factory("АвтоВаз", available_models_factory)
models_in_order = ["Веста", "Гранта", "Нива", "БМВ"]
quantity = randint(10, 30)

order = Order(factory, models_in_order, quantity)

dealer = Dealer("Элвис", 10)
dealer.create_order(order)
factory.get_info_amount_created_cars()
