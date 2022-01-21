class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __repr__(self):
        # nice way of printing
        return f'TreeNode ({repr(self.value)})'

class BinarySearchTree:
    def __init__(self):
        # binary search tree initialized with root pointing to None
        self.root = None

    # using an iterative approach
    def insert(self, new_node):
        # special case: empty tree
        # if root is None, set root to new node and return
        if self.root is None:
            print(f'Special case: new root--> {new_node}')
            self.root = new_node
            return
        # General case: non-empty tree
        print(f'Searching for location to insert--> {new_node}')
        # want a current_node pointer, starting at root to walk down the tree checking for the right spot
        current_node = self.root
        # Loop until an insert is made
        while True:
            print(f'current_node is now {current_node}')
            # if value < current node value
            if new_node.value < current_node.value:
                print("Trying left")
                # if current node left is None
                if current_node.left is None:
                    # insert new_node and break loop
                    print('Nothing here, inserting left')
                    current_node.left = new_node
                    break
                # left is full, move the pointer
                else:
                    # set current node to current_node.left
                    print("Occupied, moving current_node left")
                    current_node = current_node.left
            # if value > current node value
            else:
                print("Trying right")
                # if current node.right is None
                if current_node.right is None:
                    # insert new_node and break the loop
                    print('Nothing here, inserting right')
                    current_node.right = new_node
                    break
                # right is full, move the pointer
                else:
                    # set current node to current_node.right
                    print("Occupied, moving current_node right")
                    current_node = current_node.right

    # iterative search through bst
    def search(self, value):
        current_node = self.root
        while current_node:
            # base case: we found the node
            if value == current_node.value:
                return current_node

            if value < current_node.value:
                # move left
                current_node = current_node.left
            else:
                # move right
                current_node = current_node.right
        # loop broke, node not found
        return None

    # recursive search:
    def search_recursive(self, value):
        # helper function to pass in a node
        def helper(node):
            # Did we fall off the end of the tree?
            if node is None:
                # we've gotten to the end, haven't found the target value
                return None
            
            # Is this what we are looking for?
            if node.value == value:
                # found our target value, recursive calls stop here and we start returning to empty call stack
                return node

            # Otherwise, repeat the search of the left branch of node
            if value < node.value:
                # return whatever the search to the left gave
                return helper(node.left)
            else:
                # return whatever a search to the right gave
                return helper(node.right)

        # invoke the helper search function on tree root and return its result
        return helper(self.root)

    # get maximum height of tree, smallest version of this problem:
    # height = maximum of the left subtree heigh and right subtree height plus the root's height (always 1)
    # return height
    def get_max_height(self):

        # helper function makes recursion easier
        def recursion_helper(node):
            # edge case if tree is empty
            # also a base case: if the height of the tree is 1, the node passed in will take a max height of the left and right subtrees. Since the left and right subtrees are both None, their heights are 0, and we return 0
            if node is None:
                return 0
            
            # compute left_height: runs this function all the way down the left branch, once node.left is passed in and is None, we've hit the bottom of the left subtree. The call stack is full and starts returning starting at 0 (code above triggered as the current node is None) and incrementing by one on each return of height below until we have a left_height
            left_height = recursion_helper(node.left)
            # compute right_height
            right_height = recursion_helper(node.right)

            # from our smallest version of the problem plan
            # if run on single node, left subtree and right subtree are both None and have return 0 for their heights, 1 is then added on for the root node and returned
            height = max(left_height, right_height) + 1
            return height
        
        # return the result of our helper function being called on the root of the tree
        return recursion_helper(self.root)
        


'''
Demo Tree
                10
              /    \
             5      15
                   /   \
                  11       
'''
bst = BinarySearchTree()
print('--------------')
bst.insert(TreeNode(10))
print('--------------')
bst.insert(TreeNode(5))
print('--------------')
bst.insert(TreeNode(15))
print('--------------')
bst.insert(TreeNode(11))
print('--------------')
print(bst.search(15)) # TreeNode (15)
print(bst.search(99)) # None

print(bst.get_max_height()) # 3
