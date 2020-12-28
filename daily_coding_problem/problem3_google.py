"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        print(self.val)
        if self.left and self.right:
            self.left.print_tree()
            self.right.print_tree()
        elif self.left:
            self.left.print_tree()
        elif self.right:
            self.right.print_tree()



def serialize(node, s=""):
    s += str(node.val) + ","
    if node.left and node.right:
        s = serialize(node.left, s)
        s = serialize(node.right, s)
    elif node.left:
        s = serialize(node.left, s)
    elif node.right:
        s = serialize(node.right, s)
    elif not node.left and not node.right:
        s += "/,"
    return s
# ----Alternate solution which, I realize, is simpler---
# def serialize(node, s=""):
#     if node:
#         s += str(node.val) + ","
#         s = serialize(node.left, s)
#         s = serialize(node.right, s)
#     return s

i = 0

# s = "1,2,4,/,5,/,3,6,/,7,8,/,"
def deserialize(s):

    global i
    if s[i] == '/':
        if i < (len(s)-3):
            i += 2
        return None
    else:
        node = Node(s[i])
        # skipping the commas so incrementing by 2 instead of 1
        i += 2
        node.left = deserialize(s)
        node.right = deserialize(s)
    return node


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node('c')
root.right.right = Node('b')
root.right.right.right = Node('a')

root.print_tree()

string = serialize(root)
print(f" the serialized tree is: {string}")
tree = deserialize(string)
tree.print_tree()










# ----- OLD STUFF - IGNORE ------

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# # define root node
# node = Node(10, 5, 12)
#
# #           10
# #          /  \
# #        5     15
# #      /   \  /  \
# #     3    8 12   17

#
# class Node:
#
#     def __init__(self, data):
#
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
#         print(self.data)
#         print(data)
# # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                     print(self.data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()
#
# # Use the insert method to add nodes
# root = Node(10)
# root.insert(5)
# root.insert(11)
#
#
# # root.PrintTree()

