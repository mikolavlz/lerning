from random import randint
from pasport import passport
class Passport_office:

    def __init__(self, quantity):
        # self.number = number
        # self.serial = serial
        # self.fio = fio
        self.quantity = quantity
        self.list_pass = []

    def create_passport(self,quantity):
        new_pass = ()
        fio_create = ''
        self.quantity = quantity
        for i in range(0, self.quantity):
                fio_create = input("введите фамилию ")
                if input("Хотите ввсети серию вручную введите h") == "h":
                    serial = input("Серия :")
                else:
                    serial = (randint(1111, 9999))
                new_pass = (serial , randint(111111, 999999), fio_create)
                self.list_pass.append(new_pass)
                print(f'Создан паспорт сер:{serial} номер:{new_pass[1]} фамилия:{fio_create}')
        return self.list_pass

    #пытался сделать проверку повторения номеров через цикл while но не догадался как проверять ввод - начинаю проверку с пустого
    # списка обьектов и цикл for перебирает от 0 до 0 сделовательно не рабатет . Добавлять обьект в список до проверки тоже неправильно
    # , добавлять проверку на пустой список обьектов кажется тоже не верное решение и увеличит сложность алгоритма .

    # def create_passport(self, quantity):
    #     new_pass = ()
    #     fio_create = ''
    #     self.quantity = quantity
    #     for i in range(0, self.quantity):
    #         err = 1
    #         while err == 1:
    #             fio_create = input("введите фамилию ")
    #             if input("Хотите ввсети серию вручную введите h") == "h":
    #                 serial = input("Серия :")
    #             else:
    #                 serial = (randint(1111, 9999))
    #             new_pass = (serial, randint(111111, 999999), fio_create)
    #             for n in range(0, len(self.list_pass)):
    #
    #                 if new_pass[1] == str(self.list_pass[i][1]) or new_pass[0] == str(self.list_pass[i][0]):
    #                     print('Серия или номер уже есть пробуй еще')
    #                     print(new_pass[1],self.list_pass[i][1])
    #                     print(err)
    #                     break
    #                 else:
    #                     err = 0
    #                     self.list_pass.append(new_pass)
    #                     print(f'Создан паспорт сер:{serial} номер:{new_pass[1]} фамилия:{fio_create}')
    #     return self.list_pass

    def find_pass_nomer(self,number): #получаем номер из main
        print(f'ищем по номеру {number}')
        find = 0 # пока еще ничего не нашли
        for i in range(0, len(self.list_pass)):
             if str(number) == str(self.list_pass[i][1]): #сравниваем номер
                print(f'по номеру {self.list_pass[i][1]} найдена фамиия {self.list_pass[i][2]}')
                find = 1 #указывем что нашли совпадение
                break    #заканчиваем перебор
        if find == 0:    #если ничего не нашли
            print("ничего не найдено")

    def find_pass_serial(self,number):
        print(f'ищем по серии {number}')
        find = 0
        for i in range(0, len(self.list_pass)):
            if number == str(self.list_pass[i][0]):
               print(f'по серии {self.list_pass[i][0]} найдена фамиия {self.list_pass[i][2]}')
               find = 1
               break
        if find == 0:
            print('ничего не найдено')
