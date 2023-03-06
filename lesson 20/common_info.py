my_list = [2,5,4,6,4,7,78,3,5,3,6,3,7]
# new_list = []
# for item in my_list:
#     new_list.append(item+10)
# print(new_list)


# new_list = [item+10 for item  in my_list]
# print(new_list)

new_list = [item for item  in my_list if item %2 != 0]
print(new_list)

# # для получения случайного числа в произвольном отрезке
# from random import random
# # random() * (max- min) +1
# print(random()* 9 +1)

# from functools import reduce
# def my_funk(curent, next):
#     return curent + next
# # print(reduce(my_funk,(my_list)))

# from itertools import count
# for item in count(5):
#     if item >15:
#         break
#     else:
#         print(item)



from itertools import cycle
c = 0
for item in cycle('ABC'):
    if c > 10:
        break
    print(item)
    c += 1
