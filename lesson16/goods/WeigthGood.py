from Item import Good

class WeigntGood():
    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity

    def get_final_price(self):
        return self.price * self.quantity