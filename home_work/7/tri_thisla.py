lst = ['124','234','435','675']
print("\n".join(lst))
fnd = input('введите число для поиска ')
if lst.__contains__(fnd):
    print(f'индекс числа в списке {lst.index(fnd)}')
else:
    print('число не найдено')