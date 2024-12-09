class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def duplicate_nodes(self):
        current = self.head
        while current:

            new_node = Node(current.data)

            new_node.next = current.next
            current.next = new_node

            current = new_node.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)


ll.print_list()

ll.duplicate_nodes()

ll.print_list()


