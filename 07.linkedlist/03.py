class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return


        current = self.head
        while current.next and current.next.data <= data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty priority queue")
        min_data = self.head.data
        self.head = self.head.next
        return min_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty priority queue")
        return self.head.data

    def print_queue(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


pq = PriorityQueue()
numbers = [5, 1, 3, 8, 2, 6]
for num in numbers:
    pq.enqueue(num)

pq.print_queue()

print("Dequeue:", pq.dequeue())

pq.print_queue()
