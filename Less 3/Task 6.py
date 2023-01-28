digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
two_list = digits + symbol

acset_one = digits[-1] + digits[-1]
acset_two = digits[0] + symbol[-3]
acset_tree = digits[-3] + symbol[2]
acset_four = digits[1] + digits[5]
acset_five = symbol[0] + digits[0]
acset_six = symbol[2] + digits[-3]

string = [acset_one, acset_two, acset_tree, acset_four, acset_five, acset_six]

# letter_a = two_list.index('A')
# letter_b = two_list.index('B')
# letter_c = two_list.index('C')
# letter_d = two_list.index('D')
# letter_e = two_list.index('E')
# letter_f = two_list.index('F')
# letter_g = two_list.index('G')

# letter_zero = two_list.index('0')
# letter_one = two_list.index('1')
# letter_two = two_list.index('2')
# letter_three = two_list.index('3')
# letter_four = two_list.index('4')
# letter_five = two_list.index('5')
# letter_six = two_list.index('6')
# letter_seven = two_list.index('7')
# letter_eight = two_list.index('8')
# letter_nine = two_list.index('9')

# acset_one = two_list.index('0'), two_list.index('0')
# acset_one = ''.join(acset_one)
# acset_two = two_list[letter_one], two_list[letter_e]
# acset_two = ''.join(acset_two)
# acset_tree = two_list[letter_eight], two_list[letter_c]
# acset_tree = ''.join(acset_tree)
# # acset_four = two_list[letter_two], two_list[letter_six]
# acset_four = ''.join(acset_four)
# acset_five = two_list[letter_a], two_list[letter_one]
# acset_five = ''.join(acset_five)
# acset_six = two_list[letter_c], two_list[letter_eight]
# acset_six = ''.join(acset_six)

print(':'.join(string))
