# access to Binary Search Tree is through the root node
# all nodes are essentially a property derviced from the root node variable

# class for individual node in the Binary Search Tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # init new node with value passed in
        new_node = BSTNode(value)
        # find where the value should be in the tree
        if self.value > value:
            # check if child exists
            if self.left is None:
                self.left = new_node
            else:
                # move the job of inserting down a level
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = new_node
            else:
                # move the job of inserting down a level
                self.right.insert(value)

    def search(self, target):
        # base case
        if self.value == target:
            return self
        # base case not run, call the function again on appropriate child node
        elif self.value > target:
            # we've gotten to the bottom of this path of the tree and the target isn't there
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        # base case not run, call the function again on appropriate child node
        else:
            # we've gotten to the bottom of this path of the tree and the target isn't there
            if self.right is None:
                return False
            else:
                return self.right.search(target)

root = BSTNode(8)

root.insert(5)
root.insert(10)
print("root", root.value)
print("left", root.left.value)
print("right", root.right.value)

root.insert(12)
root.insert(9)
root.insert(1)
root.insert(6)

print(root.search(9).value)
print(root.search(99))