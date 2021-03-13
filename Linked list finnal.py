class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def append_items(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def insert_item(self, index, data):
        if index < 0 and index >= self.size():
            raise Exception("Invalid input")
        if index == 0:
            self.head = self.insert_at_beggining(data)
        count = 0
        current = self.head
        while current is not None:

            if count == index - 1:
                node = Node(data, current.next)
                current.next = node
            count += 1
            current = current.next

    def remove_item(self, index):
        if index < 0 and index >= self.size():
            raise Exception("Invalid input")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while current is not None:
            if count == index - 1:
                current.next = current.next.next
            current = current.next
            count += 1

    def print_list(self):
        my_list = []
        current = self.head
        while current is not None:
            my_list.append(current.data)
            current = current.next
        return my_list

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                print("fount it".upper())
                return True
            else:
                current = current.next
        print("Not here")
        return False


linked_list = LinkedList()
print("this is the finnal example of linked list\n\n".upper())

number_of_item = int(input("how many nodes do you want in your list : "))
for i in range(0, number_of_item):
    inputs = str(input(f'enter item no {i + 1} : '))
    linked_list.append_items(inputs)

print(f'\nYour Linked list : {linked_list.print_list()}\n\n')
print("you can insert, remove and set new heads in your list".capitalize())
options = input("do you want to update (y or n) : ")
if options == "y" or options == "Y":
    print("""\nwhat do you want?\n
1-> Insert item
2-> Remove item
3-> Update head 
    """)
    update_options = int(input("please provide option number : "))
    if update_options == 1:
        index = int(input("please provide index number : "))
        data = str(input("please enter the data for your node : "))
        linked_list.insert_item(index, data)
        print(f'your updated Linked list {linked_list.print_list()}')
    elif update_options == 2:
        index = int(input("please provide index number that you want to remove : "))
        linked_list.remove_item(index)
        print(f'your updated Linked list {linked_list.print_list()}')
    elif update_options == 3:
        data = str(input("please provide the head node"))
        linked_list.insert_at_beggining(data)
        print(f'your updated Linked list {linked_list.print_list()}')
elif options == "n" or options == "N":
    print("\nok then, have a great day")
else:
    print("invalid input")
