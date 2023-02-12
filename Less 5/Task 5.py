hour = int(input('Введите часы: '))
minutes = int(input('Введите минуты: '))
seconds = int(input('Введите секунды: '))

if 0 <= hour <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    if hour <= 9:
        if minutes <= 9:
            if seconds <= 9:
                print(f'0{hour}:0{minutes}:0{seconds}')
            else:
                print(f'0{hour}:0{minutes}:{seconds}')
        elif minutes > 9 and seconds <= 9:
            print(f'0{hour}:{minutes}:0{seconds}')
        elif minutes > 9:
            print(f'0{hour}:{minutes}:{seconds}')
    elif hour > 9 and minutes > 9 and seconds <= 9:
        print(f'{hour}:{minutes}:0{seconds}')
    elif hour > 9 and minutes > 9 and seconds <= 9:
        print(f'{hour}:{minutes}:0{seconds}')
    elif hour > 9 and minutes and seconds <= 9:
        print(f'{hour}:0{minutes}:0{seconds}')
    elif hour and seconds > 9 and minutes <= 9:
        print(f'{hour}:0{minutes}:{seconds}')
    else:
        print(f'{hour}:{minutes}:{seconds}')
else:
    print('"Введите числа для часов от 0 до 23, и для минут и секунд от '
          '0 до 59')
