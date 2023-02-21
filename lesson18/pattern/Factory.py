class Coffee:
    def grind_coffee(self):
        print("Пермаклыфвание зерен")
    def make_coffee(self):
        print("Приготовление кофе")
    def pass_coffee(self):
        print("Передача кофе клиенту")
class Cappuchino(Coffee):
    def __init__(self):
        self.grind_coffee()
        self.make_coffee()
        self.pass_coffee()
    def make_coffee(self):
        super().make_coffee()
        print("Добавляем молоко")

class Latte(Coffee):
    def __init__(self):
        self.grind_coffee()
        self.make_coffee()
        self.pass_coffee()
    def make_coffee(self):
        super().make_coffee()
        print("Добавляем много молока")

class Ammerikano(Coffee):
    def __init__(self):
        self.grind_coffee()
        self.make_coffee()
        self.pass_coffee()
    def make_coffee(self):
        super().make_coffee()
        print("Добавляем  корицу")

class CoffeeFactory:
    def get_coffee(self,type_coffee):
        if type_coffee == "Латте":
            coffee = Latte()
        if type_coffee == "Капучино":
            coffee = Cappuchino()
        if type_coffee == "Американо":
            coffee = Ammerikano()
        return coffee

class CoffeeStore:
    def make_order(self, coffee_type):
        coffee = CoffeeFactory().get_coffee(coffee_type)
        if coffee != None:
            print(f"ваш кофе {coffee_type} готов")

CoffeeStore().make_order("Американо")


