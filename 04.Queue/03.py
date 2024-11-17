import random

class Queue:
    def __init__(self, max_size=100):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            self.queue.append(item)
        else:
            raise OverflowError("Queue is full")

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.queue)

queue1 = Queue()
queue2 = Queue()


for i in range(random.randint(1, 100)):
    queue1.enqueue(random.randint(1, 100))

for j in range(random.randint(1, 100)):
    queue2.enqueue(random.randint(1, 100))

total_size = queue1.size() + queue2.size()

if total_size > 100:
    print("Total elements exceed 100. Reducing the number of elements.")
    while total_size > 100:
        if queue1.size() > 0:
            queue1.dequeue()
        elif queue2.size() > 0:
            queue2.dequeue()
        total_size = queue1.size() + queue2.size()

print("Final size of Queue 1:", queue1.size())
print("Final size of Queue 2:", queue2.size())
