import random
import threading
import time

import rx
from rx import operators, scheduler
from rx.core.run import run
from rx.subject import Subject

observable01 = rx.of('333', '4444', '22', '55555')
composed_observable = observable01.pipe(rx.operators.map(lambda s: len(s)), rx.operators.filter(lambda i: i >= 3))
composed_observable2 = observable01.pipe(rx.operators.filter(lambda s: len(s) >= 3))
observable01.subscribe(lambda value: print(f'source: {value}'))
composed_observable.subscribe(lambda value: print(f'composed: {value}'))
composed_observable2.subscribe(lambda value: print(f'composed2: {value}'))

print('-----------------------------')

subject_source = Subject()
subject_source_filtered = subject_source.pipe(rx.operators.filter(lambda v: len(v) <= 4))
subject_source.subscribe(lambda value: print(f'subject_source: {value}'))
subject_source_filtered.subscribe(lambda value: print(f'subject_source_filtered: {value}'))
subject_source.on_next('333')
subject_source.on_next('4444')
subject_source.on_next('55555')
subject_source.on_next('22')

print('-----------------------------')

thread_pool_scheduler = rx.scheduler.ThreadPoolScheduler()

def some_function(value):
    time.sleep(random.randint(2, 10) * 0.1)
    return value + 1

observable02 = rx.from_iterable(range(0, 6, 1))
observable03 = rx.from_iterable(range(10, 60, 10))
observable04 = observable02.pipe(rx.operators.map(lambda x: some_function(x)), rx.operators.subscribe_on(thread_pool_scheduler))
observable05 = observable03.pipe(rx.operators.map(lambda x: some_function(x)), rx.operators.subscribe_on(thread_pool_scheduler))

observable04.subscribe(lambda i: print(f'{threading.current_thread().name} {i}'))
observable05.subscribe(lambda i: print(f'{threading.current_thread().name} {i}'))
