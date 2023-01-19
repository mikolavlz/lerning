# сначала фаил открыть
file = open('c:/test/test.txt','w')
print(type(file))
#для записи используем write
file.write('Java\nPython\nPHP')
file.close()