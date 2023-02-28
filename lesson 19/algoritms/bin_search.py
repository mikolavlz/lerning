def bin_search(items,x):
    i = 0
    j = len(items)
    m = int(j/2)

    while items[m] != x and i<=j:
        if x > items[m]:
            i = m+1
        else:
            i =  m-1
        m = int((i +j)/2)

        return  i

print (bin_search([1,2,3,4,6,7,8,9],9))

