# Задача №1

data_lst = ['1', '2', '3', '4d', 5]
output_lst = []
for data in data_lst:
    try:
        num = int(data)
        output_lst.append(num)
    except ValueError:
        print(f"\n'{data}' ({data_lst.index(data)+1}-й элемент списка данных) невалиден")
print(output_lst, end="\n\n")

# Задача №2


def clear_numbers(number_phone):
    number_phone = number_phone.replace('(', '').replace(')', '')
    number_phone = number_phone.replace(' ', '').replace('-', '')

    if number_phone.startswith('+7'):
        number_phone = number_phone[1:]
    return number_phone


phone_list = []

phone_numbers = input('Введите номера телефонов через точку с запятой (без пробелов):\n').split(';')
for number in phone_numbers:
    phone_number = clear_numbers(number)
    if not phone_number.isdigit():
        raise ValueError(f'номер {number} должен состоять только из цифр')
    if not len(phone_number) == 11:
        raise ValueError(f'номер {number} должен составлять 11 знаков')
    if not (phone_number[0] == '8' or phone_number[0] == '7'):
        raise ValueError(f'номер {number} должен начинаться с 8 или +7')
    if phone_number[0] == '7':
        phone_list.append('+'+phone_number)
    else:
        phone_list.append(phone_number)
print(phone_list)
