"""Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.output = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recursive(node):
            
            if not node:
                return False

            left = recursive(node.left)
            right = recursive(node.right)

            if node == p or node == q:
                mid = True
            else:
                mid = False

            if mid + left + right >= 2:
                self.output = node

            return mid or left or right

        recursive(root)
        return self.output
