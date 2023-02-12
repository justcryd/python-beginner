months = ('', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
          'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

if 1 < int(number := input('Введите строку: ')) > 12:
    print('Введите число от 1 до 12')
elif not (3 <= int(number) <= 11):
    print('Зима', months[int(number)])
elif 3 <= int(number) < 6:
    print('Весна', months[int(number)])
elif 5 < int(number) < 9:
    print('Лето', months[int(number)])
elif 8 < int(number) < 12:
    print('Осень', months[int(number)])
