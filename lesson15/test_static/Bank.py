class Bank:
    def __init__(self,money):
        self.money = money

    @staticmethod
    def get_profit(money,count_years,rate):
        return count_years * (money *rate / 100)

class VTB(Bank):
    def __init__(self, money):
        super().__init__(money)
    @staticmethod
    def get_profit(money):
        return money * 1.2
vtb = VTB(1000000)
# print(vtb.get_profit(vtb.money))
print(Bank.get_profit(vtb.money,10,7)) #статические методы класса можно запускать по имени класса потомка