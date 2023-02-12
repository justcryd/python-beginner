#random_string = input('Введите строку: ')

#if len(random_string) <= 1:
#    print(f'В строке {len(random_string)} символ')
#elif 1 < len(random_string) <= 4:
#    print(f'В строке {len(random_string)} символа')
#elif 5 <= len(random_string) <= 100:
#    print(f'В строке {len(random_string)} символов')
#else:
#    print('Количество символов не должно быть больше 100!')

if len(random_string := input('Введите строку: ')) > 100:
    print('Количество символов не должно быть больше 100!')
elif len(tuple(random_string)) == 1:
    print(f'В строке {len(random_string)} символ')
elif 2 <= len(tuple(random_string)) <= 4:
    print(f'В строке {len(random_string)} символа')
elif 5 <= len(tuple(random_string)) <= 100:
    print(f'В строке {len(random_string)} символов')

print(len(tuple(random_string)))
