user_number = int(input('Введите возраст: '))

if 1 <= user_number <= 6:
    print('Детство это - прекрасно!')
elif 7 <= user_number <= -17:
    print('Учиться, учиться, учиться...')
elif 18 <= user_number <= 64:
    print('Теперь ты можешь делать всё что угодно!')
elif 65 <= user_number <= 100:
    print('Заслуженный отдых')
else:
    print('Введите число от 1 до 100')
