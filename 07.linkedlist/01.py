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


    def delete_max(self):
        if self.head == None:
            return
        max = self.head
        max_prev = None

        current_node = self.head
        prev_Node = None

        while current_node:
            if max.data < current_node.data:
                max = current_node
                max_prev = prev_Node
            prev_Node = current_node
            current_node = current_node.next

        if max_prev is None:
            self.head = max.next
        else:
            max_prev.next = max.next



linkedList = linked_list()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)

linkedList.print_list()
linkedList.delete_max()
linkedList.print_list()
