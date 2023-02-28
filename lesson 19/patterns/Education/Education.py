from abc import ABC , abstractmethod

class Education(ABC):
    def template_lern(self):
        self.enter()
        self.study()
        self.pass_exams()
        self.get_document()

    def pass_exams(self):
        print("сдаем впускные экзамены")

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def get_document(self):
        pass

class Shcool(Education):


    @abstractmethod
    def enter(self):
        print("Поступаем без экзаменов")

    @abstractmethod
    def study(self):
        print("Ходим на уроки")

    def get_document(self):
        print("Получаем доумент")


class Univer(Education):

    @abstractmethod
    def enter(self):
        print("Сдаем экзамены")

    @abstractmethod
    def study(self):
        print("Ходим на пары")

    def get_document(self):
        print("Получаем диплом")

# school = Shcool()
# school.template_lern()

univer = Univer()
Univer.template_lern()

