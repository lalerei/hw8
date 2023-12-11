from pick_file import pick_number_file


def change_row():
    numf = pick_number_file()
    with open(f"db/data_{numf}.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

    count_rows = len(data)
    if count_rows == 0:
        print("Файл пуст!")
    else:
        number_row = int(input(f"Введите номер строки от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(
                input(f"Ошибка!" f"Введите номер строки" f"от 1 до {count_rows}: ")
            )
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        patronymic = input("Введите отчество: ")
        telnum = input("Введите номер телефона: ")

        data[
            number_row - 1
        ] = f"{number_row}; {name}; {surname}; {patronymic}; {telnum}\n"
        with open(f"db/data_{numf}.txt", "w", encoding="utf-8") as file:
            file.writelines(data)

        print("Данные изменены!")
