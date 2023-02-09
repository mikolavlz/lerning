# методы класса похож на обычный метод , но имеющий доступ ко всем полям класса . Данный метод
# привязан к к классу а не обьекту класса .

class MyClass:
    x = 10 #свойство класса
    @classmethod
    def test(cls): #с помощю cls можно обращаться к полям и методам класса
        print(cls.x)
        cls.usualy(cls) #таким бразом мы запускае методы обьектов из метода класса
        cls.my_static()
        cls.demo()
    def usualy(self):
        self.x = MyClass.x
        print("test")

    @staticmethod
    def my_static():
        print("Static metod")

    @classmethod
    def demo(cls):
        print ("test metod class")

MyClass.test()