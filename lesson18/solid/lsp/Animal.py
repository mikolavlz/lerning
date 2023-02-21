class Animal:
    def __init(self,name):
        self.name = name
    def voisce(self):
        print("Издать звук")

    def play(self):
        print("Выполнит ькоманду")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def voisce(self):
        print("Мяу")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def voisce(self):
        print("ГАф")

cat = Cat("Барсик")
dog = Dog("Бобик")
animals = [cat,dog]
for animals in animals:
    Animal.voisce()


