list_title = input('введите название блюд через запятую').split(',')
my_dict = {}
for i in range(0,4):
    my_dict[i] = list_title[i-1]
answer = input (f'введите название блюда из списка {".".join(my_dict.values())}')
for key,value in my_dict.items():
     if value == answer:
         my_dict.pop(key)
         break
print(my_dict)