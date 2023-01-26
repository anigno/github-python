import rx
from rx import Observable
from rx.core import Observer
from rx.core.abc import Scheduler
from rx.disposable import Disposable
from rx.subject import Subject

def subscribe_function(observer: Observer, scheduler: Scheduler) -> Disposable:
    observer.on_next('A')
    observer.on_next('B')
    observer.on_next('C')
    observer.on_next('D')
    observer.on_next('E')
    observer.on_completed()
    return Disposable()

observable01 = rx.create(subscribe_function)

observable01.subscribe(
        on_next=lambda i: print(f'on_next: {i}'),
        on_error=lambda i: print(f'on_error: {i}'),
        on_completed=lambda: print(f'on_completed'))
print('------------------------------------------')

observable02 = rx.of(1, 2, 3, 4)
observable02.subscribe(lambda i: print(f'on_next: {i}'))
print('------------------------------------------')

# first to emit will be propagated, other will be ignored
observable03 = rx.amb(observable01, observable02)
observable03.subscribe(lambda i: print(f'on_next: {i}'))
print('------------------------------------------')

# combine the latest emitted values from each observable
s1 = Subject()
s2 = Subject()
observable04 = rx.combine_latest(s1, s2)
observable04.subscribe(lambda i: print(f'on_next: {i}'))
s1.on_next('A')
s2.on_next(1)
s2.on_next(2)
s1.on_next('B')
s1.on_next('C')
s2.on_next(3)
print('------------------------------------------')

# like for function
observable05 = rx.generate(3, lambda x: x < 7, lambda x: x + 1)
observable05.subscribe(lambda i: print(f'on_next: {i}'))
print('------------------------------------------')

def func():
    return True

# uses one of two observables according to condition function
observable06 = rx.if_then(func, observable01, observable02)
observable06.subscribe(lambda i: print(f'on_next: {i}'))
print('------------------------------------------')

observable08=rx.merge(observable01,observable02)
observable08.subscribe(lambda i: print(f'on_next: {i}'))
print('------------------------------------------')

observable09=rx.from_iterable([10,20,30,40,50])
observable09.subscribe(lambda i: print(f'on_next: {i}'))
print('------------------------------------------')


observable07 = rx.interval(1.0)
observable07.subscribe(lambda i: print(f'on_next: {i}'))

input('press enter to exit\n\n')

print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
