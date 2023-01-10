# Преобразование кортежа в список
# numbers = 10,20,30,40,50,60
# print(type(numbers))
# mylist = list(numbers)
# print(mylist)

# x = [1,2,3] * 5
# print(x)

# s = "test "
# print (s * 3)

# Обход списка
# numbers = 10,20,30,40,50,60
# for item in numbers:
#     print(item)

# # range(start,end,step) - создает числа
# print(list(range(0,11,2)))

# lang = ["java","JS","C#"]
# i=1
# for item in langs:
#     print()

# # Сравнить 2 списка
# list1 = [1,2,3,4,5]
# list2 = range(1,6)
# if list1 == list2:
#     print("Одинаковые")
# else:
#     print("разные")

# Добавление элемента
# list1 = [1,2,3,4,5]
# list1.append(6)
# list1.insert(0,0)
# print(list1)

# Сортирова списка

# my_list = ['ccc','55','bbb']
# my_list.sort() #прямая соритровака
# print(my_list)
# my_list.reverse() #обратная соритровка
# print(my_list)

#заполним рандомными

# from random import randint
# my_list = []
# count = 0
# for item in range(10):
#     number = randint(1,10)
#

# # поиск элемента в списке
# lang = ["java","JS","C#"]
# print("JS" in lang)  #in проверяет элемент в списке
# # поиск элемента в списке 2 способ __contains__
# print(lang.__contains__(("C#")))

# удаление элемента из списка
# pop - удаляет последний элемент в списке и возврашает его
# lang = ["java","JS","C#"]
# remover_item = lang.pop(-1)
# print(remover_item)
# print(lang)

#remove
# lang = ["java","JS","C#"]
# lang.remove("JS")
# print(lang)

#Создать оофис с сотрудниками котрые получают рандомный оклад
from random import randint
def create_office(adress,count):
    print(f"V office{adress} work {count}")
    office = []
    for i in range(count):
        salary = randint(70000,100000)
        print(f"sotrudnik # {i + 1} zarabatyvaet {salary}")
        office.append(salary)
    return office
office1 = create_office(" Moskow 1",10)
office2 = create_office(" Lenin20",20)
office3 = create_office(" Kiev 54", 15)
company = [office1,office2,office3]
# print(company)

print(office1)
def
office1.sort()
print(office1[-1])
