from marvel import full_dict
from typing import *
from pprint import pprint

user_list = list(map(lambda num: int(num) if num.isdigit() else None, input('Введите цифры через пробел\n').split()))
user_dict: Dict[int, Dict[str, str | int]] = dict(filter(lambda user_id: user_id if user_id[0] in user_list else None, full_dict.items()))
print('Пользовательский словарь по id (п.3 ДЗ):')
pprint(user_dict, sort_dicts=False)

input('Нажмите "Enter" для продолжения\n')

set_director: Set[str] = set(filter(lambda director: director, [i['director'] for i in full_dict.values()]))
print('Set comprehension по ключу "director" (п.4 ДЗ):')
pprint(set_director, sort_dicts=False)

input('Нажмите "Enter" для продолжения\n')

dict_year: Dict[int, Dict[str, str]] = dict(map(lambda item: (item[0], dict(map(lambda key: (key[0], str(key[1]) if key[0] == 'year' else key[1]), item[1].items()))), full_dict.items()))
print('Dict comprehension c применением функции str к "year" (п.5 ДЗ):')
pprint(dict_year, sort_dicts=False)

input('Нажмите "Enter" для продолжения\n')

dict_title_ch: Dict[int, Dict[str, Any]] = dict(filter(lambda item: item[1]['title'].startswith('Ч'), full_dict.items()))
print('Dict comprehension фильмов на букву "Ч" (п.6 ДЗ):')
pprint(dict_title_ch, sort_dicts=False)

input('Нажмите "Enter" для продолжения\n')

dict_sort_producer: Dict[int, Dict[str, str | int]] = dict(sorted(full_dict.items(), key=lambda item: item[1]['producer']))
print('Сортировка словаря по одному параметру "producer" (п.7 ДЗ):')
pprint(dict_sort_producer, sort_dicts=False)

input('Нажмите "Enter" для продолжения\n')

dict_sorted_two: Dict[int, Dict[str, str | int]] = dict(sorted(full_dict.items(), key=lambda x: (x[1]['director'], x[0])))
print('Сортировка словаря по двум параметрам - "director" и id (п.8 ДЗ):')
pprint(dict_sorted_two, sort_dicts=False)

input('Нажмите "Enter" для продолжения\n')

dict_sorted_filter: Dict[int, Dict[str, Any]] = dict(sorted(filter(lambda x: x[1] if len(x[1]['title'].split()) == 2 else None, full_dict.items()), key=lambda x: x[1]['director']))
print('Сортировка по параметру "director" словаря с фильтром по названию фильма, состоящего из двух слов (п.9 ДЗ):')
pprint(dict_sorted_filter, sort_dicts=False)

print('\nПроверку mypy прошло, но пришлось для этого прописать аннотацию типов в импортируемом full_dict')
