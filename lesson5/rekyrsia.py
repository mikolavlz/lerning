def show_numbers(n):
    print(n)
    if n == 1:
        return
    show_numbers(n-1)
show_numbers(994)