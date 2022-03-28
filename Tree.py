class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def insert(self, child):
        child.parent = self
        self.children.append(child)
    def print(self):
        print(self.data)

def buid_product_tree():
    root = Tree("electronics")
    laptop = Tree("laptop")
    root.insert(laptop)
    return root



buid_product_tree()
