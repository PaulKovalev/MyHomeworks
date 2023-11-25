from marvel import full_dict

stage = {
    1: "Первая фаза",
    2: "Вторая фаза",
    3: "Третья фаза",
    4: "Четвертая фаза",
    5: "Пятая фаза",
    6: "Шестая фаза"
}

request = input('Введите номер фазы:\n')
if not request.isdigit():
    raise TypeError('Пожалуйста введите цифру')
if int(request) > 6:
    raise ValueError('Такой фазы не существует')

stage_phase = stage[int(request)]

print(f'\n{stage_phase}:\n')
for i in full_dict:
    if stage_phase in full_dict[i].values():
        [print(key, value, sep=' : ') for key, value in full_dict[i].items()]
        print()
