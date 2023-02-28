class Builder:
    def build_body(self):
        pass
    def build_engine(self):
        pass
class Auto:
    def __init__(self,body,engine):
        self.__isEngine = False #по умолчанию выключен
        self.__body = body
        self.__engine = engine

    def on(self):
        if self.__isEngine == False:
            self.__isEngine = True
            print(f"Двигатель запустили ")
    def off(self):
        self.__isEngine = False
        print('Двигатель остановили')
    def __str__(self):
        info = "включен" if self.__isEngine else "выключен"
        return f"Двигатель у автомобиля {info} "
        self.__body = body
        self.__engine = engine
class Body:
    def __init__(self, color):
        self.color = color
    """Кузов"""
class Engine:
    def __init__(self,capacity):
        self.capacity = capacity
    """Двигатель"""

class Builder:

    def builed_body(self,color):
        self.color = color
        return Body(color)
    def builed_engine(self,capacity):
        self.capacity = capacity
        return Engine(capacity)

    def create_builder(self,color,capacity):
        body = self.builed_body(color)
        engine = self.builed_engine(capacity)
        print(f"Создаем автомобиль с цветом: {color}, и обьемом двигателя {capacity}")
        return Auto(body, engine)
builder = Builder()
Auto = builder.create_builder("Красный","2L")
Auto.on()
print(Auto)
