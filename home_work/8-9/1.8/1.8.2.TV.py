tv_list = ["Поле чудес","Новости","Доброе утро","Кинопанорама"]
print(('\n'.join(tv_list)))
tv = input("Введи название телепередеачи ")
position = int(input("Введи номер позиции в списке "))
tv_list.insert(position,tv)
print(('\n'.join(tv_list)))