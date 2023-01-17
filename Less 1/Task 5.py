home_yura = 7 * 9  # прямоугольный дом с длиной стен 7х9 метров.
home_alexander = 3.14 * ((9 ** 2) / 4)  # круглый дом диаметром 9 метров
home_vladimir = (6 * 3) + (6 * 8)  # неправильная форма на рисунке 2

check_yura = (home_alexander <= home_yura) and (home_yura >= home_vladimir)
check_vladimir = (home_yura <= home_vladimir) and (home_vladimir >=
                                                   home_alexander)
check_alexander = (home_yura <= home_alexander) and (home_alexander >=
                                                     home_vladimir)

print('У Юрасика самый маленький домишка', check_yura)
print('У Вовчика самый маленький домишка', check_vladimir)
print('У Шурика самый маленький домишка', check_alexander)
