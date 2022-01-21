# given the root node of a binary tree, find its minimum depth
# min_depth is the number of nodes along the shortest path from the root to the nearest leaf node
import collections

# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def min_depth(root):
    # make sure we have a tree
    if not root:
        return 0
    # make a queue using deque
    q = collections.deque()
    # add the root node to the queue as an array with the node as index 0 and level as index 1
    q.append([root, 1])
    # while items are in the queue
    while q:
        # pop the node from the queue and deconstruct the array to node, level
        node, level = q.popleft()
        # if there is no node.left and no node.right return the depth
        if node.left is None and node.right is None:
            return level
        if node.left:
            # append new array [node.left, level + 1]
            q.append([node.left, level + 1])
        if node.right:
            # append new array [node.right, level + 1]
            q.append([node.right, level + 1])
        





def min_depth_recursive(root):
    # define a base case: no root we're at a null node, return 0
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    # keep asking the question until we get to the bottom level
    left_depth = min_depth_recursive(root.left)
    right_depth = min_depth_recursive(root.right)

    # we've started returning
    return min(left_depth, right_depth) + 1

r = Tree(5)
r.left = Tree(7)
r.right = Tree(22)
r.right.right = Tree(9)
r.right.left = Tree(17)

# print(min_depth_recursive(r)) #--> 2
print(min_depth(r)) #--> 2
