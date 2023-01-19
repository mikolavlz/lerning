# # сначала фаил открыть
# file = open('c:/test/test.txt','w')
# print(type(file))
# #для записи используем write
# file.write('Java\nPython\nPHP')
# file.close()

# # второй способ
# with open('c:/test/test.txt','w') as file :
#     file.writelines(['newstr1\n','newstr2\n','newstr3\n'])

# считываем строки
# read- считывает
# readline- считывает первую строку
# readlines - сяитываем строки в список и досуп по индексу
with open('c:/test/test.txt','r') as file :
    # print(file.readlines()[2])
    for line in file:
        print(line,end=' ')