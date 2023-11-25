request_to_continue = 'yes'
while ('д' in request_to_continue) or ('y' in request_to_continue):
    palindrome_check = input('Введите слово:\n')
    if palindrome_check.lower() == palindrome_check[::-1].lower():
        print(f'Обнаружен палиндром: {palindrome_check}\n')
    else:
        print(f'Слово "{palindrome_check}" не является палиндромом!\n')
    request_to_continue = input('Продолжить ввод слов? (Да/Нет) : ').lower()
