class Student:
    def __init__(self,fio,cource):
        self.__fio = fio
        self.__cource = cource
        self.univer = "MGU"

    @property
    def fio(self):
        return  self.__fio

    @property
    def cource(self):
        return self.__cource

    @fio.setter
    def fio(self,fio):
        self.__fio= fio


    @cource.setter
    def cource(self,cource):
        if 1 <= cource <=5:
            self.__cource = cource
        else:
            print("error")