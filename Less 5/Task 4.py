random_string = input('Введите строку: ')

if len(random_string) <= 1:
    print(f'В строке {len(random_string)} символ')
elif 1 < len(random_string) <= 4:
    print(f'В строке {len(random_string)} символа')
elif 5 <= len(random_string) <= 100:
    print(f'В строке {len(random_string)} символов')
else:
    print('Количество символов не должно быть больше 100!')
