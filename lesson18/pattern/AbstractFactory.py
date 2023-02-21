class AbstractFactory:
    def get_food(self):
        pass
    def get_drink(self):
        pass

class Drink:
    def __init__(self,title):
        self.__title = title
    def __str__(self):
        return self.__title
class Food:
    def __init__(self,title):
        self.title = title
    def __str__(self):
        return self.__title
class ConcreateFactory1(AbstractFactory):
    def __init__(self):
        print(self.get_drink())
        print(self.get_food())
    def get_food(self):
        return Food("Бургер")
    def get_drink(self):
        return Drink("КОфе")

class ConcreateFactory2(AbstractFactory):
    def __init__(self):
        print(self.get_drink())
        print(self.get_food())
    def get_food(self):
        return Food("Чизбургер")
    def get_drink(self):
        return Drink("КОла")

def GetFacroty(number_order):
    if number_order == 1:
        return ConcreateFactory1
    elif number_order == 2:
        return  ConcreateFactory2

factory = GetFacroty(1)

