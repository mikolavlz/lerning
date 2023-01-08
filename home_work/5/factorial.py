def fuck(n):
    if n == 1:
        return n
    else:
        return n * fuck(n - 1)
print(fuck(3)*(fuck(8)+fuck(4)))