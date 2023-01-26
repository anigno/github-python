import rx
from rx import operators

observable01 = rx.from_list([1, 2, 3, 4])
# f(g(x))
observable02 = observable01.pipe(rx.operators.filter(lambda x: x % 2 == 0), rx.operators.map(lambda x: x * 2))
# g(f(x))
observable03 = observable01.pipe(rx.operators.map(lambda x: x * 2), rx.operators.filter(lambda x: x % 2 == 0))

observable01.subscribe(lambda i: print(f'observable01: {i}'))
print('-----------------------------')
observable02.subscribe(lambda i: print(f'observable02: {i}'))
print('-----------------------------')
observable03.subscribe(lambda i: print(f'observable02: {i}'))
