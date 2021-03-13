# using lists for making stack is an unoptimised way of implementing it
# because lists in python are dynamic array and it takes a lot of space in case of new item addition
# therefore using the deque method is an optimised option
# deque method is built with double linked list so it has O(1) complexity

from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()

for charecter in "hello my friend":
    stack.push(charecter)

new =""
for charecter in range(stack.size()):
    new += stack.pop()
print(new)