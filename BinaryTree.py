class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        if data == self.data:
            return
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinaryTreeNode(data)
        else:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinaryTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        if self.left:
            elements += self.left.post_order_traversal()
        return elements

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def sum_of_elems(self):
        elements = 0
        if self.right:
            for i in self.right.post_order_traversal():
                elements += i
        elements += self.data
        if self.left:
            for i in self.left.post_order_traversal():
                elements += i
        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BinaryTreeNode()
    for node in elements:
        root.insert(node)
    return root


if __name__ == "__main__":
    a = build_tree([19, 8, 3, 5, 200])

    print(a.search(19))
    print(a.find_max())
    print(a.find_min())
    print(a.sum_of_elems())
    print(a.post_order_traversal())
    a.delete(8)
    print(a.in_order_traversal())
