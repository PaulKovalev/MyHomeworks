from typing import *
import csv


# Домашнее задание. Часть 1


def password_checker(func: Callable) -> Callable:
    def wrapper(*args):
        password = str(*args)

        if password.isalnum():
            raise ValueError('Пароль должен содержать хотя бы один спецзнак')
        elif password.find(' ') != -1:
            raise ValueError('Пароль не должен содержать пробелов')
        elif password.isupper() or password.islower():
            raise ValueError('Пароль должен содержать символы разных регистров (большие и маленькие)')
        elif len(password) < 8:
            raise ValueError('Пароль должен быть не менее 8 символов')
        elif True not in set(map(lambda x: x.isdigit(), password)):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif True not in set(map(lambda x: x.isalpha(), password)):
            raise ValueError('Пароль должен содержать хотя бы одну букву')

        return func()
    return wrapper


@password_checker
def register_user():
    return print("Пароль надежный. Регистрация успешна!")


register_user(input('Введите пароль\n'))


# Домашнее задание. Часть 2


def password_validator(func: Callable, length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1) -> Callable:
    """
    Декоратор для валидации паролей.
    Параметры:
    length (int): Минимальная длина пароля (по умолчанию 8).
    uppercase (int): Минимальное количество букв верхнего регистра (по умолчанию 1).
    lowercase (int): Минимальное количество букв нижнего регистра (по умолчанию 1).
    special_chars (int): Минимальное количество спец-знаков (по умолчанию 1).
    """

    def wrapper(*args):
        password = ''.join(args[1].split())

        if len(password) < length:
            raise ValueError('Увеличьте длину пароля')
        if sum(map(str.isupper, password)) < uppercase:
            raise ValueError('Увеличьте количество букв верхнего регистра')
        if sum(map(str.islower, password)) < lowercase:
            raise ValueError('Увеличьте количество букв нижнего регистра')
        if (len(password) - sum(map(str.isalnum, password))) < special_chars:
            raise ValueError('Увеличьте количество спец-знаков')
        return func(*(args[0], password))
    return wrapper


def username_validator(func: Callable) -> Callable:
    def wrapper(*args):
        username = args[0]
        if username.find(' ') != -1:
            raise ValueError('Имя пользователя не должно содержать пробелы')
        return func(*args)
    return wrapper


@username_validator
@password_validator
def register_user2(username: str, password: str):
    """
    Функция для регистрации нового пользователя.
    Параметры:
    username (str): Имя пользователя.
    password (str): Пароль пользователя.
    ValueError: Если пароль или юзернейм не соответствует заданным условиям.
    """

    with open('reg.csv', 'a', newline='') as reg:
        writer = csv.writer(reg, delimiter=':')
        writer.writerow((username, password))


try:
    register_user2(input('Введите имя пользователя\n'), input('Введите пароль\n'))
    print('Регистрация прошла успешно!')
except ValueError as error:
    print(f'Ошибка: {error}')
