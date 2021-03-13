#  Linked list is a data structure which is better than traditional arrays
# Array are lists where data is stored in a consecutive manner in main memory
# suppose you have to insert an item in middle of an array then you will have to shift all the items of array
# linked lists stores data in a non-consecutive manner  in data segments
# these data segments are called nodes
# nodes contain a data section and a next pointer section which points to next node
# Linked lists starts with a head node and with null

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_node(self):
        print(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append_nodes(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        print_list = []
        node = self.head
        while node is not None:
            print_list.append(node.data)
            node = node.next
        return print_list

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                print("found it")
                return True
            else:
                current = current.next
        print("not here")
        return False

    def size(self):
        current = self.head
        total = 0
        while current is not None:
            total += 1
            current = current.next
        return total


linked_list = LinkedList()

print("this is an example of linked list\n\n".upper())
items = int(input("How many items do you want in your linked list : "))
for i in range(0, items):
    charecter_item = str(input(f'enter item no {i + 1} :  '))
    linked_list.append_nodes(charecter_item)

print(linked_list.print_list())
print(f'the size of the list is {linked_list.size()}')
