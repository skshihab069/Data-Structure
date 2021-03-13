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


stack = Stack()
string = input("Give any string :")

for i in string:
    stack.push(i)

new = ""
for i in range(len(stack.list)):
    new += stack.pop()

print(f'The reversed string is : {new}')
