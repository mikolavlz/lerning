class Builder:
    def build_body(self):
        pass
    def build_lamp(self):
        pass
    def build_battery(self):
        pass
    def build_fonarik(self):
        pass
class Fonarik:
    def __init__(self,body,lamp,battery):
        self.__on = False #по умолчанию выключен
        self.__body = body
        self.__lamp = lamp
        self.__battery = battery

    def on(self):
        self.__on = True
    def off(self):
        self.__on = False
    def __str__(self):
       info =   "вкл" if self.__on else "выкл"
       return f"Фонарик {info}"
class Lamp:
    """Лампочка"""
class Body:
    """Кораус"""
class Battery:
    """Батарейцка"""

class BuilderFonarik:
    def builed_body(self):
        return Body()
    def builed_lamp(self):
        return Lamp()
    def builed_battery(self):
        return Battery()
    def create_builder(self):
        body = self.builed_body()
        lamp = self.builed_lamp()
        battery = self.builed_battery()
        return Fonarik(body,lamp,battery)
builder = BuilderFonarik()
fonarik = builder.create_builder()
fonarik.on()
print(fonarik)


