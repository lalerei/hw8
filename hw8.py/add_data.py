from pick_file import pick_number_file


def add_row():
    numf = pick_number_file()
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    telnum = input("Введите номер телефона: ")
    with open(f"db/data_{numf}.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        now_number_row = len(data) + 1

    with open(f"db/data_{numf}.txt", "a", encoding="utf-8") as file:
        file.write(f"{now_number_row};{name};" f"{surname};{patronymic};{telnum}\n")
    print("Данные записаны!")
