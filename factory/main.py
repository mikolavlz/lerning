# подсчет машин и проверку моделей произвожу в классе order
from random import randint

from factory.Diller import Dealer
from factory.Factory import Factory
from factory.Order import Order

factory = Factory("АвтоВаз")
models_in_order = ["Веста","Гранта","Нива","БМВ"]
quantity = randint(10,30)

order = Order(factory, models_in_order, quantity)


dealer = Dealer("Элвис",11)
dealer2 = Dealer("АвтоМаркет",9)


dealer.create_order(order)
dealer2.create_order(order)

