class Passport:
    def __init__(self,number,series,fio):
        self.number = number
        self.series = series
        self.fio = fio
    def get_info(self):
        return f"Гражданин {self.fio} имеет паспорт №{self.number} серия {self.series}"
