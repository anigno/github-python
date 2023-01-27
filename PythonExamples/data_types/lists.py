# cutting a list
a = 'abcdefg'
print(a[2:5])  # cde
print(a[:3])  # abc
print(a[:])  # abcdefg
print(a[:-2])  # abcde
print(a[-5:-2])  # cde
print(a[-15:15])  # abcdefg (no error)
print(a[2: 8: 2])  # ceg

# concat a list
b = a * 2
print(b)  # abcdefgabcdefg
c = b + b
print(c)  # abcdefgabcdefgabcdefgabcdefg

# find in list
a = [5, 4, 6, 3, 8]
print(3 in a)  # True
print(9 in a)  # False

# enumerate
for index, item in enumerate(a):
    print(f'[{index} {item}]', end=' ')  # [0 5] [1 4] [2 6] [3 3] [4 8]
print()

# min max
print(min(a))  # 3
a = ['pig', 'egg', 'dog', 'mouse']
print(max(a))  # pig

# in place sorting
a.sort()
print(a)  # ['dog', 'egg', 'mouse', 'pig']
a.sort(reverse=True)
print(a)  # ['pig', 'mouse', 'egg', 'dog']
a.sort(key=lambda i: i[1])  # sorted by second letter
print(a)  # ['egg', 'pig', 'mouse', 'dog']

# out of place sorting
b = sorted(a, key=lambda i: i[2])  # sorted by third letter
print(b)  # ['egg', 'pig', 'dog', 'mouse']

# counting and summing
print(a.index('mouse'))  # 2
a = 'abaacfbacbd'
print(a.count('a'))  # 4
print(a.count('b'))  # 3
a = [2, 4, 3, 2, 5]
print(sum(a))  # 16

# unpacking list
b, c, d, e, f = a
print(b, c, d, e, f)  # 2 4 3 2 5

# list comprehension
a = [i for i in range(0, 30, 3)]
print(a)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
b = [i * i for i in a if i % 2 == 0]
print(b)  # [0, 36, 144, 324, 576]

# deleting
del (b[2])
print(b)  # [0, 36, 324, 576]
del (b[1:3])
print(b)  # [0, 576]

# add and remove
b.append(111)  # append to end of list (like push in stack)
b.extend([333, 444])
print(b)  # [0, 576, 111, 333, 444]
print(b.pop())  # 444
print(b)  # [0, 576, 111, 333]
b.remove(111)  # exception if not exists
print(b)  # [0, 576, 333]

# reverse
b.reverse()
print(b)  # [333, 576, 0]
# from collections import OrderedDict

# multi type
a = [1, 2, [3, 4], 5, 'hello']
print(a)  # [1, 2, [3, 4], 5, 'hello']
a[2][0] = 55
print(a)  # [1, 2, [55, 4], 5, 'hello']

# length
print(len(a))  # 5
a.clear()
print(len(a))  # 0
print()

# stack
stk = list()
stk.append(3)
stk.append(2)
stk.append(4)
stk.append(1)
for _ in range(4):
    print(stk.pop(), end=' ')  # 1 4 2 3
print()

# queue
queue = list()
queue.insert(0, 3)
queue.insert(0, 2)
queue.insert(0, 4)
queue.insert(0, 1)
for _ in range(4):
    print(queue.pop(), end=' ')  # 3 2 4 1
print()

