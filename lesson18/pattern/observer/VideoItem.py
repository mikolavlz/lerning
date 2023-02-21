class Movie:
    def __init__(self,title,content):
        self.title = title
        self.content = content
    def get_info_movie(self):
        return f"Ролик{self.title}, описание ролика {self.content}"
    def play_movie(self):
        print("Ролик",self.title,"Запущен..")
