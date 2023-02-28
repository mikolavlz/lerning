from timeit import timeit
my_code = '''
a = range(100000)
b = []
for i in a :
    b.append(i ** 2)
 '''

execution_time = timeit(my_code,number = 100) / 100
print(execution_time)