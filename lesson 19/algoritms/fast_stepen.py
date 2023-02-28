def stepen(a,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        res = stepen( a,n/2)
        return res * res
    return a * stepen(a, n-1)



print(stepen(2,3))