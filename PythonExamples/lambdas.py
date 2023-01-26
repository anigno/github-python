def findNumbers(predicate):
    for i in range(0, 100):
        if predicate(i):
            yield i


def lambdaEleven():
    return lambda i: i % 11 == 0


lambdaThree = lambda i: i % 3 == 0

numbersEleven = findNumbers(lambdaEleven())
numbersThree = findNumbers(lambdaThree)

for n in numbersEleven:
    print(n, end=',')

print("\n")

for n in numbersThree:
    print(n, end=',')
