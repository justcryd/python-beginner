car_speed = 30
km = 1000
man_speed = 4
man_time = 2

min_to_sec = 10 * 60
distance_metr = car_speed * min_to_sec  # авто от А до Б едет 10 минут 30 м/c
distance_km = distance_metr / km
remains_km = distance_km - (man_speed * man_time)  # получаем оставшиеся
# километры спустя 2 часа ходу со скорость 4 км/чэ
remains_time = remains_km / man_speed

print('Человеку осталось идти со скоростью 4 км/ч', remains_time, 'часа')
