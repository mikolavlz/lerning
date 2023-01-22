with open('matr.txt','r') as file :
    for line in file:
        print(line)
        list = line.split(' ')
        for i in range(0,5):

            # a = int(line[i])**2
            print(line[i])