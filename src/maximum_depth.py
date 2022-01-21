"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""

class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# make an example tree test case
root = BinaryTreeNode(5)
root.right = BinaryTreeNode(32)
root.right.right = BinaryTreeNode(4)
root.right.left = BinaryTreeNode(8)
root.left = BinaryTreeNode(12)

def maxDepth(root_node):
    # base case run on simpleist tree, start counting at 1
    if root_node.left is None and root_node.right is None:
        return 1
    # init depth counters
    left_depth = 0
    right_depth = 0

    # run the base case node on the children
    if root_node.left:
        left_depth = maxDepth(root_node.left)
    if root_node.right:
        right_depth = maxDepth(root_node.right)

    return max(left_depth, right_depth) + 1

print(maxDepth(root)) # 3
