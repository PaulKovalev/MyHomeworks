# Задача №1

phone_number = input('Введите номер телефона: \n')
phone_number = phone_number.replace('(', '').replace(')', '')
phone_number = phone_number.replace(' ', '').replace('-', '')

res_bgn = False
len_dgt = False
res_chk = ''

if phone_number.startswith('+7'):
    phone_number = phone_number[1:]

if phone_number.startswith('8') or phone_number.startswith('7'):
    res_bgn = True

if phone_number.isdigit() and len(phone_number) == 11:
    len_dgt = True

if res_bgn and len_dgt:
    res_chk = 'Правильный формат ввода'
else:
    res_chk = 'Формат ввода неправильный'

print(res_chk)


# Задача №2

password = input('Введите пароль: \n')

sgn_chk = False
spc_chk = False
reg_chk = False
len_chk = False
result = ''

if not password.isalnum():
    sgn_chk = True
else:
    result = 'Пароль должен содержать хотя бы один спецзнак'

if password.find(' ') == -1:
    spc_chk = True
else:
    result = 'Пароль не должен содержать пробелов'

if not (password.isupper() or password.islower()):
    reg_chk = True
else:
    result = 'Пароль должен содержать символы разных регистров (большие и маленькие)'

if len(password) > 7:
    len_chk = True
else:
    result = 'Пароль должен быть более 7 символов длиной'

if sgn_chk and spc_chk and reg_chk and len_chk:
    result = 'Пароль надежный'

print(result)
