class StacksUsingQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, item):
        self.queue2.append(item)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))

        self.queue1 , self.queue2 = self.queue2, self.queue1

stack = StacksUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.queue1)