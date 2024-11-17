# اگر فقط با اعمال enqueue و dequeue بخواهیم این کار را بکنیم ممکن نیست
# با استفاده از تابع insert در پایتون میتوان این برنامه را پیاده کرد اما ممکن است کمی با ماهیت صف تعارض داشته باشد


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

a = random.randint(0,100)

for i in range(0,a):
    queue1.enqueue(random.randint(1, 100))

print(queue1.queue)


queue2 = Queue(a)

while queue1.size() > 0:
        item = queue1.dequeue()
        queue2.enqueue(item)

while queue2.size() > 0:
        item = queue2.dequeue()
        queue1.queue.insert(0, item)


print(queue1.queue)

