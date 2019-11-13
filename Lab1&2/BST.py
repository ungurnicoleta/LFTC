class Node:
    def __init__(self, id=-1, symbol=""):
        self.left = None
        self.right = None
        self.id = id
        self.symbol = symbol

    # A utility function to insert a new node with the given key
    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.symbol < node.symbol:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

    # A utility function to search a given key in BST
    def search(self, root, key):
        # Base Cases: root is null or key is present at root
        if root is None or root.symbol == key:
            return root
            # Key is greater than root's key
        if root.symbol < key:
            return self.search(root.right, key)
        if root.symbol > key:
            # Key is smaller than root's key
            return self.search(root.left, key)
        return -1

    # A utility function to do inorder tree traversal
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print("\nSymbol: ", root.symbol, "\nCode:", root.id)
            self.inOrder(root.right)

    def __str__(self):
        return self.id


class BST:
    def __init__(self):
        self.count = 0
        self.root = Node()

    def insert(self, root, key):
        ID = self.root.search(root, key)
        # print("id: ", id)
        if ID != -1 and ID is not None:
            # print("ID: ", ID.id)
            return ID.id
        else:
            self.root.insert(root, Node(self.count, key))
            self.count += 1
            print("ID: ", self.count - 1)
            return self.count - 1

    def printBST(self):
        self.root.inOrder(self.root)

# bt = BST()
# first = bt.insert(bt.root, "x")
# bt.insert(bt.root, "medie")
# bt.insert(bt.root, "dispersie")
# bt.insert(bt.root, "frecventa")
# bt.insert(bt.root, "y")
# bt.printBST()
