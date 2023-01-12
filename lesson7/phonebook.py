info = ""

phone_book = {
                "Иванов":["2424234","35300464"],
                "Петров":["24211234","35311464","92882652"],
                "Сидоров":["24244234"]
             }

for fio,phones in phone_book.items():
    info = f"Абонент {fio} имеет "
    if len(phones) > 1:
        info += "телефоны: \n"
        i = 1
        for item in phones:
            info += f"{i}) {item}\n"
            i += 1
    else:
        info += f" телефон: {phones[0]}\n"

    print(info)
