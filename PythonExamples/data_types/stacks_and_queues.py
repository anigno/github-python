from queue import Queue, LifoQueue, PriorityQueue

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
# 3 2 1
print()
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())
print(queue.get())
print(queue.get())
# 1 2 3
print()
stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.get())
print(stack.get())
print(stack.get())
# 3 2 1
print()
queue = PriorityQueue()
queue.put((2, 'first', 44444))
queue.put((1, 'second', 1111))
queue.put((3, 'third'))
print(queue.get())
print(queue.get())
print(queue.get())
# 1 2 3
print()
queue.put((-2, 'm second'))
queue.put((-1, 'm first', 'hello'))
queue.put((-3, 'm third'))
while not queue.empty():
    print(queue.get())
# -3 -2 -1
