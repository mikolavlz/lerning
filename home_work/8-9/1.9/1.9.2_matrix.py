i = 1
with open('matr.txt', 'r') as file:
    list_2 = []
    for line in file:
        list_i = line.split()
        for item in list_i:
            list_2.append((int(item)**i))
        i += 1
with open('matr.txt', 'a') as file:
    file.write('\n')
    for n in range(0, 7, 3):
        file.write(f'{list_2[n]}  {list_2[n+1]}  {list_2[n+2]}\n')

