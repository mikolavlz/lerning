from timeit import timeit

#Линейный поиск
def col_ne(items):
    count = 0  #O(1)
    for i in range(len(items)): #O(n-1)
        if ((items[i-1])%2==0) or ((items[i+1]==0)): #O(1)
            count += 1 #O(1)
    return(count)

print(col_ne([1,2,3,4,5,6,7,8,9]))

#O = O(1) + O(n-1) + O(1) + O(1) = O(n+2) = O(n)

my_code = """
def col_ne(items):
    count = 0  #O(1)
    for i in range(len(items)): #O(n-1)
        if ((items[i-1])%2==0) or ((items[i+1]==0)): #O(1)
            count += 1 #O(1)
    return(count)

col_ne([1,2,3,4,5,6,7,8,9])
"""

execution_time = timeit(my_code,number = 100) / 100 #Выполняется код 100 раз, делим на 100 чтоб получить 1 раз, timeit-отключает сборщик мусора, данный модуль минимизирует выполнение 1 модуля
print(execution_time)