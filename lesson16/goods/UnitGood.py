from Item import Good


class UnitGood(Good):
    price = 100
    def __init__(self, quantity):
        super().__init__(quantity)

    def get_final_price(self):
        return self.price * self.quantity