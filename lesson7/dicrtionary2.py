#программа которая проверяе существует ли к ключь в словаре

def find_key(x,d):
    if x in d :
        print('exist')
    else:
        print('not exist')
find_key('a', {'v':1,'b':2})