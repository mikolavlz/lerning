import csv

def open_db():
    with open('db_market.csv', encoding='utf-8') as file_db:
        db = list(csv.DictReader(file_db))
        return db



def print_db():
    for values in open_db():
        print(values['Товар'],values["Цена"],values['Описание'])
def add_db():
    find = 0
    title = input("Введи название товара")
    for values in open_db():
        if values['Товар'] == title:
            print('Такой товар уже есть')
            break



def delete_db():
    find = 0
    title = input("Введи название товара")
    with open("db_market.csv", 'r', encoding='utf-8') as file_db:
        file_reader = csv.reader(file_db, delimiter=",")
        count = 0
        for row in file_reader:
            if title == row[0]:
                print(type(file_reader))
                find = 1
                break
            else:
                count += 1
        if find == 1:
            print("\n" * 100)
            print("Товар удалили")

        else:
            print("\n" * 100)
            print("Товар не найден")


key = ''
print(open_db())
while key != 'q':
    print_db()
    print('add - добавить товар | del - удалить товар | find - найти товар | q - закрыть программу ')
    key = input("Введите что нужно сделать : ")
    if key == 'add':
        add_db()
    elif key == 'del':
        delete_db()






