class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' <-> ')
            current_node = current_node.next
        print("None")

    def print_reverse(self):

        if not self.head:
            print("None")
            return


        current_node = self.head
        while current_node.next:
            current_node = current_node.next


        while current_node:
            print(current_node.data, end=' <-> ')
            current_node = current_node.prev
        print("None")


def list_convert(linkedList):

    if  not linkedList:
        return "empty list"

    else:
        current_node = linkedList.head

        while current_node.next:
            current_node = current_node.next

        print(current_node.data)
        current_node.next = linkedList.head
        linkedList.prev = current_node.next





# استفاده:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Forward:")
dll.print_list()

print("Reverse:")
dll.print_reverse()
list_convert(dll)

# dll.print_list()
