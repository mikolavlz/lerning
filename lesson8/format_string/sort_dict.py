# по ключу
my_dict = {'c':10,'a':5,'b':4}
sorter_dict_key  = sorted(my_dict.items(),key= lambda item:item[0]) # item:item[0]) - по ключу
sorter_dict_value  = sorted(my_dict.items(),key= lambda item:item[1]) # item:item[0])  - по значению

print(sorter_dict_key)
print(sorter_dict_value)