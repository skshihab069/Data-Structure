# Binary tree is a tree that can have 2 leaf nodes at max
# all the elements of binary search tree is unique
# Binary search tree has a root node
# the left node is always smaller than the root node
# the right node is always larger than the root node
# Binary search tree has O(log n) complexity

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
               return self.left

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [7, 10, 12, 23, 24, 20]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(10))
    print(numbers_tree.delete(10))
    print(numbers_tree.in_order_traversal())