from collections import namedtuple

PeriodicTaskTuple = namedtuple('PeriodicTaskDescriptor', ['taskFunction', 'periodic', 'interval'])

a = PeriodicTaskTuple('func', 4, 30)
print(a)
