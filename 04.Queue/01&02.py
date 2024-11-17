#اضافه کردن و حذف یک عنصر از صف اولویت با استفاده از heapq که از هیپ استفاده میکند دارای
#پیچیدگی زمانی O(logn) است
#جست و جوی یک عنصر خاص دارای پیچیدگی زمانی O(n) است



import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)[-1]
        raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return len(self._queue) == 0


pq = PriorityQueue()
pq.push("task1", 1)
pq.push("task2", 3)
pq.push("task3", 2)

while not pq.is_empty():
    print(pq.pop())
