import json
from typing import *


def set_from_json(json_file: Any) -> Set:
    """
    Принимает Json-файл.
    Возвращает сет из Json-файла.
    :param json_file: Json-файл
    :return: сет данных из Json-файла
    """
    with open(json_file, 'r', encoding='UTF-8') as f:
        set_json = set(json.load(f))
    return set_json


def list_from_json(json_file: Any) -> List:
    """
    Принимает Json-файл.
    Возвращает данные из Json-файла. Если файл отсутствует, возвращает пустой список.
    :param json_file: Json-файл
    :return: данные из Json-файла/пустой список
    """
    try:
        with open(json_file, 'r', encoding='UTF-8') as f:
            res = json.load(f)
        return res
    except FileNotFoundError:
        return []


def check_availability(user_line: str, symbol: str, lst: List) -> bool:
    """
    Проверяет отсутствие вхождения первого аргумента во второй,
    а также первого индекса первого аргумента в третий аргумент.
    :param user_line: Индексируемая последовательность данных
    :param symbol: Последовательность данных
    :param lst: Последовательность данных
    :return: Результат проверки - True/False
    """
    return user_line not in lst or user_line[0] not in symbol


def bad_letter(line: str) -> str:
    """
    Принимает строку.
    Возвращает в верхнем регистре последний символ в строке,
    если символ не 'ъ', 'ы', 'ь',
    либо предпоследний в противном случае.
    :param line: Строка
    :return: Последний или предпоследний символ в верхнем регистре
    """

    if line[-1] not in 'ъыь':
        last_letter = line[-1].upper()
    else:
        last_letter = line[-2].upper()
    return last_letter


def check_list_availability(symbol: str, data: List) -> bool:
    """
    Проверяет отсутствие вхождения первого аргумента
    в список первых индексов каждого из элементов второго аргумента.
    :param symbol: Последовательность данных
    :param data: Последовательность индексируемых данных
    :return: Результат проверки - True/False
    """
    return symbol not in [item[0] for item in data]


def search_word(symbol: str, data: List) -> Tuple[str, str, List]:
    """
    Ищет первый из элементов второго аргумента,
    значение первого индекса которого равно первому аргументу.
    - Удаляет этот элемент из второго аргумента
    - присваивает первому аргументу значение последнего
    индекса удаленного элемента, если значение не 'ъ', 'ы', 'ь',
    либо предпоследнего в противном случае.
    Возвращает:
    - обновленный первый аргумент
    - удаленный элемент второго аргумента
    - обновленный второй аргумент
    :param symbol: Последовательность данных
    :param data: Последовательность индексируемых данных
    :return: Последний или предпоследний символ удаленного элемента в верхнем регистре,
             удаленный элемент,
             второй аргумент без удаленного элемента
    """
    word = ''
    for item in data:
        if item[0] == symbol:
            data.remove(item)
            symbol = bad_letter(item)
            word = item
            break
    return symbol, word, data


def record_result(record: Any, lst: List) -> List:
    """
    Удаляет первый элемент из второго аргумента,
    если количество элементов равно 5.
    Добавляет первый аргумент в конец второго аргумента
    :param record: Данные
    :param lst: Список данных
    :return: Список данных с добавленным первым аргументом
    """
    if len(lst) == 5:
        del lst[0]
    lst.append(record)
    return lst


def dump_json(record: List, json_file: Any):
    """
    Записывает первый аргумент в Json-файл
    :param record: Данные, подготовленные для Json-конвертации
    :param json_file: Json-файл
    :return: не нужен
    """
    with open(json_file, 'w', encoding='UTF-8') as f:
        json.dump(record, f, ensure_ascii=False, indent=4)


def main():
    """
    Игра в города
    :return: не нужен
    """
    cities_name = set_from_json('cities.json')
    result_5games = list_from_json('result_5games.json')

    if result_5games:
        print('Результат последних пяти игр:',
              *result_5games, sep='\n', end='\n\n')

    letter = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'

    while True:
        user_city = input('Введите название города\n').strip().title()

        if check_availability(user_city, letter, cities_name):
            result = 'Вы проиграли!'
            break
        else:
            cities_name.remove(user_city)
            letter = bad_letter(user_city)
            if check_list_availability(letter, cities_name):
                result = 'Вы выиграли!'
                break
            else:
                letter, comp_city, cities_name = search_word(letter, cities_name)
                print(f'\n{comp_city}\n'
                      f'Вам на "{letter}"\n')
    print(result)

    result_5games = record_result(result, result_5games)
    dump_json(result_5games, 'result_5games.json')


main()
