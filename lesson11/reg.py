import re
txt = "the rain in moscow.moscow test ..moscow.."
x= re.findall('moscow',txt)
print(x)
# индекс первого пробела
y = re.search("\s",txt)
print(y)
str = '''
первая строка
вторая строка
треться строка
'''
string = ['строка',"вторая"]
for s in string:
    math = re.search(s,str)
    if math:
        print("найден {} в {}".format(s,math.start()))
    else:
        print('не найден')

