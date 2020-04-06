list1 = ['a', 'abc', 'xyz', 's', 'aba','1221']
list2 = [x for x in list1 if len(x) >2 if x[0] == x[-1]]
print(list2)