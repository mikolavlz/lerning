import random
def random_file_num():
    with open('rnd_num.txt','w') as file :
        i = 1
        while i < 11 :
            file.write(f'{str(random.randrange(1,999,1))}\n')
            i = i + 1
def min_max_write():
    with open('rnd_num.txt', 'r') as file:
        list_num = file.readlines()
    with open('output.txt', 'w') as file:
        file.write(f'{min(list_num)}{max(list_num)}')

random_file_num()
min_max_write()

