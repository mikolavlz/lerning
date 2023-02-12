from random import randint

from factory.Diller import Dealer
from factory.Factory import Factory
from factory.Order import Order

factory = Factory("АвтоВаз")
models_in_order = ["Веста","Гранта","Нива","БМВ"]
quantity = randint(10,30)

order = Order(factory,models_in_order,quantity)

dealer = Dealer("Элвис",20)
dealer.create_order(order)
