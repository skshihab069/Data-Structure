from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()


def place_order(listt):
    for items in listt:
        print(f"placing order for {items}")
        queue.enqueue(items)
        time.sleep(0.5)


def order_delivery():
    time.sleep(1)
    while True:
        order = queue.dequeue()
        print(f"delinering order for {order}")
        time.sleep(2)
        if queue.is_empty() is True:
            break
            return


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
t1 = threading.Thread(target=place_order(orders), args=orders)
t2 = threading.Thread(target=order_delivery())
t1.start()
t2.start()

