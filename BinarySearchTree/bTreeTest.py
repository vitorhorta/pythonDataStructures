import unittest
from BinarySearchTree import BinarySearchTree
class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.addItem(3)
        self.tree.addItem(2)
        self.tree.addItem(7)
        self.tree.addItem(1)
        self.tree.addItem(9)
        self.tree.addItem(6)
        self.resultedArray = []

    def compareValues(self,x):
        self.resultedArray.append(x)

    def testAdd(self):
        tree = BinarySearchTree()
        self.assertTrue(tree.addItem(3))

    def testPreOrderTraversal(self):
        expectedArray = [3,2,1,7,6,9]
        self.tree.preOrderTraversal(self.compareValues)
        self.assertEquals(self.resultedArray,expectedArray)

    def testInOrderTraversal(self):
        expectedArray = [1,2,3,6,7,9]
        self.tree.inOrderTraversal(self.compareValues)
        self.assertEquals(self.resultedArray,expectedArray)

    def testPostOrderTraversal(self):
        expectedArray = [1,2,3,6,7,9]
        self.tree.inOrderTraversal(self.compareValues)
        self.assertEquals(self.resultedArray,expectedArray)


if __name__ == '__main__':
    unittest.main()