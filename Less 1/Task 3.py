count_comp = 1000  # количество компьютеров в botnet сети
plus_today = 3  # добавляется каждый день
minus_today = 2  # уменьшается каждый день
days = 30  # всего дней

minus_for_all_days = days * minus_today
plus_for_all_days = days * plus_today
plus_count_comp_for_all_days = count_comp - minus_for_all_days + plus_for_all_days
minus_count_comp_for_all_days = count_comp - minus_for_all_days

print('Если не будет добавлять новых', minus_count_comp_for_all_days)
print('Если будет добавлять 3 новый каждый день', plus_count_comp_for_all_days)
