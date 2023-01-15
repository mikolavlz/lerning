prdmt = ['математика', 'литература', 'химия', 'физика', 'черчение', 'рисование']
close = 1
print(f'Какой предмет тебе не нравиться?\n{prdmt}')
while exit == 1:
    a = input('введи предмет или `хватит` ')
    if prdmt.__contains__(a):
        prdmt.pop(prdmt.index(a))
    else:
        if a == 'хватит':
            close = 0
        else:
            print('Такoго предмета нет в списке попробуй еще')
print(f'Вот что вам нраситься {prdmt}')
