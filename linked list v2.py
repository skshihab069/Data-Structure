class Node:
    def __init__(self, data=None, ):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_item(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        my_list = []
        current = self.head
        while current is not None:
            my_list.append(current.data)
            current = current.next
        return my_list

    def size(self):
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                print("Fount it !!")
                return True
            else:
                current = current.next
        print("not here ")
        return False

linked_list = LinkedList()

print("this is an example of linked list\n\n".upper())
items = int(input("how many items do you want in your list :  "))

for i in range(0, items):
    items_for_list = str(input(f'Enter item no {i+1} :  '))
    linked_list.append_item(items_for_list)

print(f'\n\nyour item list {linked_list.print_list()}'.upper())
print(f'\nthe size of list is {linked_list.size()}'.upper())
