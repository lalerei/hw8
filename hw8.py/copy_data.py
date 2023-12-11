from print_data import print_file
from pick_file import pick_number_file


def copy_row():
    numf = pick_number_file()
    with open(f"db/data_{numf}.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

    data_length = len(data_1)
    if data_length == 0:
        print("Файл пуст!")
    else:
        input_user = int(input("Введите номер строки\n" f"от 1 до {data_length}: "))
        while input_user < 1 or input_user > data_length:
            input_user = int(
                input(f"Введите номер строки \n" f"от 1 до {data_length}: ")
            )

        print()
        print("Куда копировать?")
        data_2, numf_2 = data_1()
        data_2_length = len(data_2)
        data_1 = [
            f'{data_2_length + 1};{data_1[input_user - 1].split(";")[1]};'
            f'{data_1[input_user - 1].split(";")[2]};'
            f'{data_1[input_user - 1].split(";")[3]};'
            f'{data_1[input_user - 1].split(";")[4]}'
        ]
        final_string = ";".join(data_1)
        with open(f"db/data_{numf_2}.txt", "a", encoding="utf-8") as file:
            file.write(final_string)
        print("Данные скопированы!\n")
