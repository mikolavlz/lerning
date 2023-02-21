class Subscriber:
    def __init__(self,login,chanels):
        self.login = login
        self.chanels = chanels

    def update(self,title_chanel, title_movie):
        print(self.login,"на канале", title_chanel,"появился ролик",{title_movie})