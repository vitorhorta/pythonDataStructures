from stack.Stack import Stack


def defaultTraverseAction(x):
    print(x)

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._left = None
        self._right = None

    def addItem(self, value):
        parent = self.getItem(value)
        if parent == self:
            self._root = value
            self._left = BinarySearchTree()
            self._right = BinarySearchTree()
            return True
        parent.addItem(value)

    def getItem(self, value):
        if self._root == value:
            return True

        if self._root > value and self._left != None:
            return self._left.getItem(value)

        if self._root < value and self._right != None:
            return self._right.getItem(value)

        return self

    def preOrderTraversal(self, action = defaultTraverseAction):
        if self._root != None:
            action(self._root)
            self._left.preOrderTraversal(action)
            self._right.preOrderTraversal(action)

    def inOrderTraversal(self, action = defaultTraverseAction):
        if self._root != None:
            self._left.inOrderTraversal(action)
            action(self._root)
            self._right.inOrderTraversal(action)

    def postOrderTraversal(self, action = defaultTraverseAction):
        if self._root != None:
            self._left.postOrderTraversal(action)
            self._right.postOrderTraversal(action)
            action(self._root)


    def __repr__(self):
        return str(self._root)
