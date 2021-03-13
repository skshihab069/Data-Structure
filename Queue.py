# Queue is container that follows the FIFO(First in first out) method
# pushing an item is called enqueue
# poping an item is called dequeue

class Queue:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list == []

    def enqueue(self, item):
        self.list.insert(0, item)

    def dequeue(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

queue = Queue()
for i in range(11):
    queue.enqueue(i)

print(queue.list)
print(queue.dequeue())
print(queue.list)
print(queue.size())