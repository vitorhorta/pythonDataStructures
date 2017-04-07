from __future__ import print_function
from BinarySearchTree.BinarySearchTree import BinarySearchTree
from hashing_table.BucketHashtable import BucketHashtable

# tree = BinarySearchTree()
# tree.addItem(3)
# tree.addItem(2)
# tree.addItem(7)
# tree.addItem(1)
# tree.addItem(9)
# tree.addItem(6)
#
# # tree.preOrderTraversal()
# # tree.inOrderTraversal()
# # tree.postOrderTraversal()
# tree.breadthFirstTraversal()

bhash = BucketHashtable()
bhash.addItem(3)
bhash.addItem(4)
bhash.addItem(8)
bhash.addItem(15)
bhash.addItem(19)
bhash.addItem(34)
bhash.addItem(18)
bhash.addItem(7)
bhash.addItem(73)
bhash.addItem(21)
bhash.addItem(98)
bhash.addItem(1)
bhash.addItem(2)
print(bhash)