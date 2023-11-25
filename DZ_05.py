# Секретное послание
secret_letter = [
    ['DFВsjl24sfFFяВАДОd24fssflj234'],
    ['asdfFп234рFFdо24с$#afdFFтasfо'],
    ['оafбasdf%^о^FFжа$#af243ю'],
    ['afпFsfайFтFsfо13н'],
    ['fн13Fа1234де123юsdсsfь'],
    ['чFFтF#Fsfsdf$$о'],
    ['и$##sfF'],
    ['вSFSDам'],
    ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
    ['FFэasdfтDFsfоasdfFт'],
    ['FяDSFзFFsыSfкFFf']
]

small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
             'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

decrypt_mes = []

for crypto_text in secret_letter:
    crypto_word = ''.join(crypto_text)
    decrypt_word = ''
    for let_chk in crypto_word:
        if let_chk in small_rus:
            decrypt_word += let_chk
    decrypt_mes.append(decrypt_word)

print(' '.join(decrypt_mes))
input('\nДля выхода из программы нажмите Enter')
