#ВАРИАНТ 1
print('Вариант 1')

botnet = int(input('Колличество агентов в Botnet: '))
plus = int(input('Добавляется агентов в день: '))
minus = int(input('Распознается агентов в день: '))
days = int(input('Всего дней: '))

days_minus = days * minus
days_plus = days * plus
plus_botnet = botnet - days_minus + days_plus
minus_botnet = botnet - days_minus

print(f"За {days} дней Ботнет уменьшится на {days_minus} агентов и общие число составит {minus_botnet} без добавления новых.\n"
      f"За {days} дней Ботнет уменьшится на {days_minus} агентов, но если добавлять по {plus} агентов в день, то мы получим {plus_botnet}")

#ВАРИАНТ 2
print('\n\nВариант 2')

x = int()
y = int()
n = int()

while n < 30:
    n = n + 1
    x = 1000 -  (n * 2) + (n * 3)
    y = 1000 - (n * 2)

print(f'Колличество без увеличения {y}\n'
      f'Колличество с увеличением {x}\n'
      f'Колличество дней {n}')