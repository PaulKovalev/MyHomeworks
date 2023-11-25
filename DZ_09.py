from cities import cities_list
import json

try:
    with open('cities_name.json', 'r', encoding='UTF-8') as file:
        cities_name = set(json.load(file))
except FileNotFoundError:
    cities_name = set(city['name'] for city in cities_list if city['name'][-1] not in 'ъьы')
    with open('cities_name.json', 'w', encoding='UTF-8') as file:
        json.dump(tuple(cities_name), file, ensure_ascii=False, indent=4)

try:
    with open('result_5games.json', 'r', encoding='UTF-8') as file:
        result_5games = json.load(file)
        print('Результат последних пяти игр:',
              *result_5games, sep='\n', end='\n\n')
except FileNotFoundError:
    result_5games = []

letter = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'

while True:
    user_city = input('Введите название города\n!!!'
                      '(Не вводите города с буквами "ъ", "ы", "ь" в конце слова!!!!):\n').title()

    if (user_city not in cities_name or
            user_city[0] not in letter):
        result = 'Вы проиграли!'
        break
    else:
        cities_name.remove(user_city)
        if user_city[-1].upper() not in [comp_city[0] for comp_city in cities_name]:
            result = 'Вы выиграли!'
            break
        else:
            for comp_city in cities_name:
                if comp_city[0] == user_city[-1].upper():
                    cities_name.remove(comp_city)
                    letter = comp_city[-1].capitalize()
                    print(f'\n{comp_city}\n'
                          f'Вам на "{letter}"\n')
                    break
print(result)

if len(result_5games) == 5:
    del result_5games[0]
result_5games.append(result)
with open('result_5games.json', 'w', encoding='UTF-8') as file:
    json.dump(result_5games, file, ensure_ascii=False, indent=4)
