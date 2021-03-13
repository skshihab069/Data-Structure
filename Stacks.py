# Stacks are containers that insert and remove data from one end only
# meaning the data last inserted is removed first
# it follows the LIFO(Last in First Out) method
# [1, 2, 3, 4] here 4 is inserted last so only it can removed, without removing the last item other items can,t be removed
# inserting an item is called pushing
# removing an item is called poping

class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list == []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def peek(self):
        last = len(self.list) - 1
        return self.list[last]


stack = Stack()

for i in range(1,11):
    stack.push(i)


print(stack.list)
print(stack.pop())
print(stack.push(11))
print(stack.list)
print(stack.peek())
print(stack.is_empty())
