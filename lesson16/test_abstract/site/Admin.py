from Template import Template


class Admin(Template):
    def __init__(self, title, description):
        super().__init__(title, description)

    def content(self):
        print("Название страницы админки:",self.title,"\nСодержимое страницы:",self.description)

