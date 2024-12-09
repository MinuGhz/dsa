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

def combine_list(list1, list2):

    if not list1.head:
        return list2

    if not list2.head:
        return list1

    result_list = linked_list()
    result_list.head = list1.head

    current_node = list1.head
    while current_node.next:
        current_node = current_node.next

    current_node.next = list2.head

    return result_list



first_list = linked_list()
second_list = linked_list()

first_list.append(1)
first_list.append(3)
first_list.append(5)

second_list.append(2)
second_list.append(4)
second_list.append(6)


third_list = combine_list(first_list, second_list)
first_list.print_list()

third_list.print_list()
