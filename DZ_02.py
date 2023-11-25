# homework№1

time_in_sec = int(input('Введите количество секунд: '))
print(f'\nВ указанном количестве секунд ({time_in_sec}):\n'
      f'Часов: {time_in_sec//3600}\n'
      f'Минут: {(time_in_sec%3600)//60}\n'
      f'Секунд: {time_in_sec%60}\n')


# homework№2

degrees_celsius = int(input('Введите температуру в градусах Цельсия: '))
print(f'\nВ указанном количестве градусов Цельсия ({degrees_celsius}):\n'
      f'Градусов Кельвина: {(degrees_celsius+273.15):.2f}\n'
      f'Градусов Фаренгейта: {(degrees_celsius*9/5+32):.2f}\n'
      f'Градусов Реомюра: {(degrees_celsius*0.8):.2f}')
