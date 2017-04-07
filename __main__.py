from __future__ import print_function
from BinarySearchTree.BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()
tree.addItem(3)
tree.addItem(2)
tree.addItem(7)
tree.addItem(1)
tree.addItem(9)
tree.addItem(6)

# tree.preOrderTraversal()
# tree.inOrderTraversal()
# tree.postOrderTraversal()
tree.breadthFirstTraversal()
