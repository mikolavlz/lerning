class Dealer:
    def __init__(self, title_dealer, age):
        self.title_dealer = title_dealer
        self.age = age

    # order - объект класса Заказ для описания всех нюансов заказа, например, количество авто и др
    def create_order(self, order):
        order.start(self.age)
        order.show_info()
