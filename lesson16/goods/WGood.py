from Item import Good

class WGood():
    def __init__(self,price,q):
        self.price = price
        self.q = q

    def get_final_price(self):
        return self.price * self.quantity