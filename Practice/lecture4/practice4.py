d = {'name': 'Armen', 'age': 15, 'grades': [10, 8,8, 4, 6, 7]}
if 'weight' not in d:
    n = int(input('write a number: '))
    d['weight'] = n
    print(d)
else:
    print(d['weight'])