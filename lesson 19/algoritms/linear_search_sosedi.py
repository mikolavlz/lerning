#сложность = O(n)
def NOTeven_number(n):
    if n % 2 == 0:
        return False
    else:
        return True
def lin_search(numbers):
    k = 0
    for item in range(len(numbers)):
        if item == 0:                              #если число первое
            if NOTeven_number(numbers[item+1]):
                k += 1
        elif item == len(numbers)-1:               #если число последнее
            if NOTeven_number(numbers[item-1]):
                k += 1
        else:
            if NOTeven_number(numbers[item-1]) or NOTeven_number(numbers[item+1]):
                k += 1
    return k

print ('Чисел с нечетными соседями = ',lin_search([1,2,3,4,5,7,9,1,1,1,1,1,1,1,1,1]))
            