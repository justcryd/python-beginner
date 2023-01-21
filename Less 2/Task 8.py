sting_one = 'четырёхсотпятидесятисемимиллиметровое'
sting_one_start = sting_one[0]
sting_one_finish = sting_one[-1]
sting_two = 'метоксихлордиэтиламинометилбутиламиноакридин'
sting_two_start = sting_two[0]
sting_two_finish = sting_two[-1]
sting_tree = 'автомотовелофототелерадиомонтёр'
sting_tree_start = sting_tree[0]
sting_tree_finish = sting_tree[-1]
sting_for = 'автоэлектростеклоподъемники'
sting_for_start = sting_for[0]
sting_for_finish = sting_for[-1]

print(sting_one, sting_one_start, sting_one_finish, sting_one.
      count(sting_one_start) + sting_one.count(sting_one_finish))
print(sting_two, sting_two_start, sting_two_finish, sting_two.
      count(sting_two_start) + sting_two.count(sting_two_finish))
print(sting_tree, sting_tree_start, sting_tree_finish, sting_tree.
      count(sting_tree_start) + sting_tree.count(sting_tree_finish))
print(sting_for, sting_for_start, sting_for_finish, sting_for.
      count(sting_for_start) + sting_one.count(sting_for_finish))
