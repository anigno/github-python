a = {2, 3, 2, 3, 2, 4}
print(a)  # {2, 3, 4}
a.add(2)
a.add(5)
print(a)  # {2, 3, 4, 5}

a.remove(3)
print(a)  # {2, 4, 5}

print(2 in a)  # True

a = {2, 4, 5}
b = {2, 4, 6}
print(a & b)  # {2, 4}
print(a | b)  # {2, 4, 5, 6}
print(a ^ b)  # {5, 6}
print(a - b)  # {5}
print(b - a)  # {6}
print(a <= b)  # False (sub set of teh other)
print(a >= b)  # False(sub set of teh other)
