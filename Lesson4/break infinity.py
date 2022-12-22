sum = 0
while True:
    number = input("введите число или стоп для выаода суммы \n")
    if number.isdigit():
        number =int(number)
        if number %2 == 0:
            sum += number
        else:
            print("вы ввели нечетное число")
            break
    else:
        if (number.lower() == "стоп"): # lower - нижни й регистр
            print("сумма равна =" , sum)
            break

