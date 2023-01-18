# Типы данных int, str: Задание 3. 30 Баллов


var_1, var_2, var_3 = 29, 738, 1005
var_1_str = str(var_1)
var_1_int = int(var_1) % 10
var_2_str = str(var_2)
var_2_int = int(var_2) // 10 % 10
var_3_str = str(var_3)
var_3_int = int(var_3) // 1000

print('Последняя цифра числа', var_1)
print('вариант 1:', var_1_str[-1])
print('вариант 2:', var_1_int)

print('Вторая цифра числа', var_2)
print('вариант 1:', var_2_str[1])
print('вариант 2:', var_2_int)


print('Первая цифра числа', var_3)
print('вариант 1:', var_3_str[0])
print('вариант 2:', var_3_int)
