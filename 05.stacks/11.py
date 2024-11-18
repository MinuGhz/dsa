class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        # self.stack1.append(item)
        # while self.stack2:
        #     self.stack1.append(self.stack2.pop())
        #
        # self.stack1 , self.stack2 = self.stack2, self.stack1
        self.stack1.append(item)

    def pop(self):
        if not self.stack1:
            while self.stack2:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

queue = QueueUsingStacks()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.stack1,queue.stack2)