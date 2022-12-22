total = 0
for i in range(0,5):
    num = int(input(f"введите число №{i + 1} \n"))
    answer = input(f"желаете ссумировать число ? y/n  \n Если выйти то stop")
    if answer == 'stop':
        break
    elif answer == 'y':
        total += num
print(num)