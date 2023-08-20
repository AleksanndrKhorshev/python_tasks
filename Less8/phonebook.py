def show_menu():
    print(' 1. Распечатать справочник\n'
          ' 2. Найти телефон по фамилии\n'
          ' 3. Изменить номер телефона\n'
          ' 4. Удалить запись\n'
          ' 5. Найти абонента по номеру телефона\n'
          ' 6. Добавить абонента в справочник\n'
          ' 7. Закончить работу')
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'w', encoding='utf-8') as phb:
        for record in phone_book:
            line = ','.join(record[field] for field in fields)
            phb.write(line + '\n')


def find_by_lastname(phone_book, last_name):
    result = []
    for record in phone_book:
        if record['Фамилия'] == last_name:
            result.append(record)
    return result


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return f'Номер для {last_name} изменен на {new_number}'
    return f'Абонент с фамилией {last_name} не найден'


def delete_by_lastname(phone_book, last_name):
    removed_records = [record for record in phone_book if record['Фамилия'] == last_name]
    phone_book[:] = [record for record in phone_book if record['Фамилия'] != last_name]

    if removed_records:
        return f'Удалены записи для {last_name}'
    else:
        return f'Абонент с фамилией {last_name} не найден'


def normalize_phone_number(number):
    return ''.join(filter(str.isdigit, number))

def find_by_number(phone_book, number):
    normalized_number = normalize_phone_number(number)
    result = []
    for record in phone_book:
        record_number = normalize_phone_number(record['Телефон'])
        if normalized_number in record_number:
            result.append(record)
    return result



def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    data = user_data.split(',')
    if len(data) == len(fields):
        new_record = dict(zip(fields, data))
        phone_book.append(new_record)
    else:
        return 'Ошибка ввода данных. Введите Фамилию, Имя, Телефон и Описание через запятую.'


def print_result(phone_book):
    for record in phone_book:
        print(f"{record['Фамилия']}, {record['Имя']}, {record['Телефон']}, {record['Описание']}")


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Фамилия: ')
            result = find_by_lastname(phone_book, last_name)
            if result:
                print_result(result)
            else:
                print(f'Абонент с фамилией {last_name} не найден')
        elif choice == 3:
            last_name = input('Фамилия: ')
            new_number = input('Новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Фамилия: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('Номер: ')
            result = find_by_number(phone_book, number)
            if result:
                print_result(result)
            else:
                print(f'Абонент с номером {number} не найден')

        elif choice == 6:
            user_data = input('Новые данные (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)

        write_txt('phonebook.txt', phone_book)
        choice = show_menu()


# Пример использования программы
work_with_phonebook()
