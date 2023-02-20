from abc import ABC,abstractmethod

class Template(ABC):
    title_site = "Блог автомобилиста"
    def __init__(self,title,description):
        self.title = title
        self.description = description
    def header(self):
        print("Шапка для сайта",self.title_site)

    def footer(self):
        print("Подвал для сайта", self.title_site)

    @abstractmethod
    def content(self):
        pass

    #выводим каждую страницу
    def render(self):
        self.header()
        self.content()
        self.footer()
        print("--------------\n")