class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linked_list:

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


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end='->')
            current_node = current_node.next

        print("None")


    def get_length(self):
        len = 0
        current_node = self.head

        while current_node:
            len += 1
            current_node = current_node.next

        return len

    def bubble_sort(self):
        current_Node = self.head
        length = self.get_length()
        itr = 0

        while itr < length:
            traverseNode = self.head
            prevNode = self.head
            swapped = False

            while traverseNode.next:
                ptr = traverseNode.next
                if traverseNode.data > ptr.data:
                    swapped = True
                    if traverseNode == self.head:
                        traverseNode.next = ptr.next
                        ptr.next = traverseNode
                        prevNode = ptr
                        self.head = prevNode
                    else:
                        traverseNode.next = ptr.next
                        ptr.next = traverseNode
                        prevNode.next = ptr
                        prevNode = ptr
                    continue
                prevNode = traverseNode
                traverseNode = traverseNode.next

            if not swapped:
                break

            itr += 1

        return self




linkedList = linked_list()
linkedList.append(20)
linkedList.append(30)
linkedList.append(3)
linkedList.append(45)

linkedList.bubble_sort()

linkedList.print_list()
