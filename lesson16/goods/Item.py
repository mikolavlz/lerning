from abc import ABC, abstractmethod

class Good(ABC):
    profit = 30  #это процент прибыли
    def __init__(self, quantity):
        self.quantity = quantity

    #Метод для получения чистой прибыли
    def get_profit(self):
        return self.get_final_price() * self.profit / 100

    @abstractmethod
    def get_final_price(self):
        pass
    