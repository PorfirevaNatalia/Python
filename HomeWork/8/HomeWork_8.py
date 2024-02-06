# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

''' чтение данных из файла'''
def read_data(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.readlines()
            return data
    except FileNotFoundError:
        print("Файл не найден!")
        return []

'''печать данных'''
def show_data(data):
    for line in data:
        print(line)

''' запись(добавление) данных в файл'''
def write_data(file_name):
    with open(file_name, "a", encoding = "utf-8") as file:
        name_contact = input("Введите имя контакта: ")
        phone_number = input ("Введите номер телефона: ")
        file.write(f"\n{name_contact} ~ {phone_number}")

''' перезапись файла (после удаления данных)'''
def rewrite_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        for line in data:
            file.write(line)

'''поиск данных'''
def find_contact(data):
    choice_user = input("Введите имя или телефон для поиска: ")
    founded = []
    for idx, line in enumerate(data):
        if choice_user.lower() in line.lower():
            print(idx, line)
            founded.append(idx)
    if len(founded) == 0:
        print("Запись не найдена")
    print(founded)
    return founded

'''выбор контакта'''
def select(data, founded):
    if len(founded) > 1:
        for i, idx in enumerate(founded):
            print(f"{idx + 1}.{data[idx]}")
            choice_user = int(input("Введите номер контакта: "))
            choice_user = founded[choice_user - 1]
    else:
        choice_user = founded[0]
    return choice_user

'''удаление контакта'''
def delete_contact(data, choice_user):
    deleted = data.pop(choice_user)
    print(f"Контакт {deleted} удален")
    return data

'''изменение контакта'''
def change_contact(data, choice_user):
    choice_for_change = input("1 - изменить имя, 2 - изменить номер: ")
    line = data[choice_user].split(" ~ ")
    print(line)
    if choice_for_change == "1":
        line[0] = input("Введите новое имя: ")
    elif choice_for_change == "2":
        line[1] = input("Введите новый номер: ")
    data[choice_user] = " \n ~ ".join(line)

'''экспорт контакта'''
def export_contact(data, choice_user):
    file_name = input("Введите имя файла: ")
    file_name = f"{file_name}.txt"
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{data[choice_user]}")

'''главное меню'''
def main():
    flag = True
    file_name = "phonebook.txt"
    while flag:
        print("0 - выход")
        print("1 - показать контакты")
        print("2 - добавить контакт")
        print("3 - найти контакт")
        print("4 - удалить контакт")
        print("5 - изменить контакт")
        print("6 - экспортировать контакт в другой файл")
        print("Выберите действие: ")
        user_choice = input()
        if user_choice == "0":
            flag = False
        elif user_choice == "1":
            show_data(read_data(file_name))
        elif user_choice == "2":
            write_data(file_name)
        elif user_choice == "3":
            find_contact(read_data(file_name))
        elif user_choice == "4":
            data = read_data(file_name)
            founded = find_contact(data)
            if len(founded) > 0:
                rewrite_file(file_name, delete_contact(data, select(data, founded)))
        elif user_choice == "5":
            data = read_data(file_name)
            founded = find_contact(data)
            if len(founded) > 0:
                change_contact(data, select(data, founded))
                rewrite_file(file_name, data)
        elif user_choice == "6":
            data = read_data(file_name)
            founded = [x for x in range(len(data))]
            export_contact(data, select(data, founded))



if __name__ == "__main__":
    main()
