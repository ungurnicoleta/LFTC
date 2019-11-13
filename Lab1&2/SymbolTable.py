from BST import BST


class ST:
    def __init__(self):
        self.tree = BST()

    def add(self, symbol):
        id = self.tree.insert(self.tree.root, symbol)
        return id


    def print(self):
        self.tree.printBST()

#
# st = ST()
# st.add("x")
# st.print()