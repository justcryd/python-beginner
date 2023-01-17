# Четверть - это 1/4 часть, то есть 25%
car_price = 11000

full_price = car_price * 4  # Вся сумма денег заработанная на BigBounty
bank = full_price * .25  # Положено в банк
purchases = full_price * .15  # разные покупки
cash_balance = full_price - car_price - bank - purchases

print('Отстаток наличными', cash_balance)
