from Person import Person


class Economist(Person):

    def __init__(self, position):
        super().__init__(position)

    def get_koefficient(self):
        return 2

