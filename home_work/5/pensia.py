import datetime
god = int(input("Веедите год своего рождения "))
def pens(god):
    print(f"Ваш возраст {(int(datetime.datetime.today().year))-god}")
    a = 65 -((int(datetime.datetime.today().year))-god)
    if a < 1:
        print("Поздравляю вы на пенсии")
    else:
        print(f"До пенсии осталось {a}")

pens(god)
