from queue import Queue, LifoQueue, PriorityQueue

stack_list = []
stack_list.append(1)
stack_list.append(2)
stack_list.append(3)
print(stack_list.pop())
print(stack_list.pop())
print(stack_list.pop())
# 3 2 1
print()
p_queue = Queue()
p_queue.put(1)
p_queue.put(2)
p_queue.put(3)
print(p_queue.get())
print(p_queue.get())
print(p_queue.get())
# 1 2 3
print()
stack_list = LifoQueue()
stack_list.put(1)
stack_list.put(2)
stack_list.put(3)
print(stack_list.get())
print(stack_list.get())
print(stack_list.get())
# 3 2 1
print()
p_queue = PriorityQueue()
p_queue.put((2, 'first', 44444))
p_queue.put((1, 'second', 1111))
p_queue.put((3, 'third'))
print(p_queue.get())
print(p_queue.get())
print(p_queue.get())
# 1 2 3
print()
p_queue.put((-2, 'm second'))
p_queue.put((-1, 'm first', 'hello'))
p_queue.put((-3, 'm third'))
while not p_queue.empty():
    print(p_queue.get())
# -3 -2 -1
