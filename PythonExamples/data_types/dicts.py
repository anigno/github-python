a = {'pork': 23.7, 'beef': 34.1, 'chicken': 16.2}
b = {(1, 10), (2, 20)}
a['shrimp'] = 44.7
print(a)  # {'pork': 23.7, 'beef': 34.1, 'chicken': 16.2, 'shrimp': 44.7}
print(b)  # {(2, 20), (1, 10)}
print('pork' in a)  # True
print(a.keys())  # dict_keys(['pork', 'beef', 'chicken', 'shrimp'])
print(a.values())  # dict_values([23.7, 34.1, 16.2, 44.7])
print(a.items())  # dict_items([('pork', 23.7), ('beef', 34.1), ('chicken', 16.2), ('shrimp', 44.7)])
print(23.7 in a.values())  # True

for k, v in a.items():
    print(f'{k}:{v}', end=' ')  # pork:23.7 beef:34.1 chicken:16.2 shrimp:44.7
print()

# sort keys
c = list(a.keys())
c.sort()
print(c)  # ['beef', 'chicken', 'pork', 'shrimp']

# dictionary comprehension
d = {i: i * i for i in range(3, 10)}
print(d)  # {3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

