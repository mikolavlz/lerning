birthday_list = []
close = 1
inp = input(f'Напиши имена 3х приглашенныхчерез пробел')
birthday_list = inp.split()
while close == 1:
    a = input('введи имя или `стоп` ')
    if a == 'стоп':
        close = 0
        print(f'Количество приглаенных = {len(birthday_list)}')
        print(birthday_list)

    else:
        birthday_list.append(a)
