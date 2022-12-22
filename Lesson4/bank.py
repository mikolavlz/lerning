money = int(input("Ваша сумма"))
years = int(input("Сколько лет"))
rate = 7 if years < 3 else 8
for year in range (1,years + 1 ):
    profit = money * rate / 100
    money += profit
    print (f"за {year} год составит {profit} , сумма = {money}\n")