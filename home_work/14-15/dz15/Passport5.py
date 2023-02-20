from random import randint

from Passport import Passport


class Passports():
    def __init__(self,count):
        self.list = []
        self.series = ""
        # self.number = number
        # self.series = series
        # self.fio = fio
        self.get_series()

        while count > 0:
            num = self.get_random_numbers(6)
            print("Номер паспорта:",num)
            if self.is_dublicate(num):
                print("Дубликат!")
                continue
            fio = input(str("Введите имя для паспорта " + self.series + " "+ " " + num))
            new_passport = Passport(num,self.series,fio)
            print(new_passport.get_info())
            self.list.append(new_passport)
            count-=1


    def is_dublicate(self,n):
        for passport in self.list:
            if passport.series == self.series and passport.number == n:
                return True
        return False

    @staticmethod
    def get_random_numbers(num):
        s = ""
        for i in range(num):
            temp = str(randint(0,9))
            s += temp
        return s

    def search(self):
        number_series = input('Введите серию и номер паспорта через пробел:').split(" ")

        # for member in self.list:
        is_find = False
        for item in self.list:
            if item.number == number_series[1] and item.series == number_series[0]:
                print(item.fio)
                is_find = True
                break
        if not is_find:
            print("Паспорт не найден")

    def get_series(self):
        cod = input("Введите код h, если хотите ввести серию сами:")
        if cod == "h":
           self.series = int(input('Введите серию паспорта:'))

        else:
            self.series = self.get_random_numbers(4)
        print("Серия паспорта:",self.series)

obj = Passports(3)
obj.search()

