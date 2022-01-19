# given the root node of a binary tree, determine if it is height-balanced
# return True if left and right sub-trees differ in height by a maximum of 1 level
# return False if left and right sub-trees differ in height by more than 1 level

# Tree nodes are defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# Plan: write another function to check base case to check if single leaf node meets the requirements of being balanced, recursively check each node all the way back up the tree
# absolute value of left sub-tree heigh and right sub-tree height MUST be <= 1
# go left and right all the way to the bottom and work our way back up
def is_balanced_tree(root):
    # define depth search function
    def height_balance(root):
        # base case: None node past the leaf is balanced with a height of 0
        # return array[0] = 0 for height since no node exists
        # and array[1] = True since it is balanced
        if not root:
            return [0, True]
        # haven't gotten to the bottom of the tree
        # ask the next nodes down to the left and right what is their height and are they balanced?
        # destructuring the return array into two variables
        left_height, left_balance = height_balance(root.left)
        right_height, right_balance = height_balance(root.right)
        
        # if we get here, we have recursed all the way down the tree and are on the way back up. we need to update the return array values to track max_height and if both sides are balanced
        max_height = max(left_height, right_height) + 1
        # for overall balance to be True left_balance must be True, right_balance must be True and the absolute difference between left_height and right_height must be <= 1
        balance = left_balance and right_balance and abs(left_height - right_height) <= 1
        return [max_height, balance]

    # run the helper function on the root and return the balance property of the return array
    return height_balance(root)[1]



    

# test cases
r = Tree(5)
r.left = Tree(10)
r.right = Tree(25)
r.right.right = Tree(3)
r.right.left = Tree(12)
print(is_balanced_tree(r)) # True

r2 = Tree(5)
r2.right = Tree(6)
r2.left = Tree(6)
r2.left.left = Tree(7)
r2.left.right = Tree(7)
r2.left.left.left = Tree(8)
r2.left.left.right = Tree(8)
print(is_balanced_tree(r2)) #False