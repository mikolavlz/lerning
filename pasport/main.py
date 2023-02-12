from pasport import passport_office

new_ps = passport_office.Passport_office(3)
print(new_ps.create_passport(3))
print('\n\n\n****')
if input("Будем искать паспорт ? y/n ") == "y": # ожидаем y или n
    if input("Ищем : посерии(1) по номеру (enter) ") == '1': #ожмдаем единицу или любой ввод
        find = input('Введие серию')
        new_ps.find_pass_serial(find) #запускаем поиск по серии
    else:
        find = input('Введие номер') #запускаем поиск по номеру
        new_ps.find_pass_nomer(find)



