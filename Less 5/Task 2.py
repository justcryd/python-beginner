user_number = int(input('Введите возраст: '))

if not (1 <= user_number) or not (user_number <= 100):
    print('Введите число от 1 до 100')
elif 1 <= user_number <= 6:
    print('Детство это - прекрасно!')
elif 7 <= user_number <= 17:
    print('Учиться, учиться, учиться...')
elif 18 <= user_number <= 64:
    print('Теперь ты можешь делать всё что угодно!')
else:
    print('Заслуженный отдых')
