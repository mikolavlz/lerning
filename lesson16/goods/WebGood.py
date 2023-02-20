from UnitGood import UnitGood


class WebGood(UnitGood):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price /= 2 #так как класс это потомок штучного товара и по условию цена в 2 раза дешевле чем у штучного

    def get_final_price(self):
        return self.price * self.quantity