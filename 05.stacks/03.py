stack = [1,2,3,4,5,6,7,8,9]
queue = []

# Enqueue the whole stack
for i in range(len(stack)):
    queue.append(stack.pop())
print(queue,stack)

# Dequeue to stack
for i in range(len(queue)):
    stack.append(queue.pop(0))
print(queue,stack)