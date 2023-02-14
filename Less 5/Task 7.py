hours = int(input('Введите часы: '))
minutes = int(input('Введите минуты: '))

if not (0 <= hours <= 23) or not (0 <= minutes <= 59):
    print('Введите правильное время')

elif not (360 <= (minutes := (hours * 60) + minutes) <= 1080):
    print('Солнце за горизонтом!')
else:
    minutes = ((minutes - 360) / 720) * 180
    print(f'Угол солнца: {minutes} градусов')
