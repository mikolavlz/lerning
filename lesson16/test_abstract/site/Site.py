from Template import Template


class Site(Template):
    def __init__(self, title, description):
        super().__init__(title, description)

    def content(self):
       print("Название страницы сайта:", self.title, "\nСодержимое страницы:", self.description)

