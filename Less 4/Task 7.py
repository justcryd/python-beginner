my_dict = {1: ("прокоп", "порок"), 2: ("сушилка", "осушка"),
           3: ("вязанка", "навязка"), 4: ("каторга", "рогатка"),
           5: ("плесень", "полдник")}

one_word_one, one_word_two = my_dict[1]
two_word_one, two_word_two = my_dict[2]
tree_word_one, tree_word_two = my_dict[3]
four_word_one, four_word_two = my_dict[4]
five_word_one, five_word_two = my_dict[5]

print(' '.join(one_word_one) >= ' '.join(one_word_two))
print(' '.join(two_word_one) >= ' '.join(two_word_two))
print(' '.join(tree_word_one) >= ' '.join(tree_word_two))
print(' '.join(four_word_one) >= ' '.join(four_word_two))
print(' '.join(five_word_one) >= ' '.join(five_word_two))
#print(' '.join(one_word_one))
