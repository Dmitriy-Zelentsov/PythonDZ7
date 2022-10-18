def get_contact():
    id = input('ID: ')
    first_name = input('Имя: ')
    second_name = input('Фамилия: ')
    position = input('Должность: ')
    salary = input('Зп: ')
    return (f'|ID|:{id}|ФИ|:{first_name} {second_name}|Должность|:{position}|ЗП|:{salary}')

def find_contact(book,serch):
    a = ''
    for line in book:
        if line.find(serch) != -1:
            a += line
    if a  == '':
        return ("Не найдено")
    else:
        return a

def request():
    return input('Запрос для поиска: ')

def mode():
    return int(input('Для записи,нажать - 1; Для поиска - 2 ; Для выхода - 0: '))

