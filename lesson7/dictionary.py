# Создание словаря
# d = dict()
# или
# d2 = {}

# my_dict = dict(ivan='admin',petr='devops')
# print(my_dict)

# 2способ
my_dict = {'ivan':'admin','petr':'devops'}
#добавление
my_dict['alex'] = 'developer'
#переопределение эл-та
my_dict['ivan'] = 'developer'
#удаление
del my_dict['petr']
#поиск эл-та по ключу
print('alex'in my_dict)
#для удаления элементов в словаре
# my_dict.clear()
#копия словаря
my_dict2= my_dict.copy()
#получение списка ключей
print(my_dict2.keys())
#получение списка значений
print(my_dict.values())
# получение ключа по значению
print(my_dict.get('ivan'))
#удаление ключа\значения
my_dict.pop('ivan')
print(my_dict)
print(my_dict2)