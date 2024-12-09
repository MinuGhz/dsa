class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):                
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "the stack is empty"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return "the stack is empty"
        return self.top.data

    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack elements:")
stack.print_stack()

print("Top element:", stack.peek())

stack.pop()
print("Stack after pop:")
stack.print_stack()
