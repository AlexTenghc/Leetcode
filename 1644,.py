"""Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node."""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.found = False

        def DFS(node):
            if not node:
                return None

            left = DFS(node.left)
            right = DFS(node.right)

            count = 0

            if node in (p, q):
                count += 1
            
            if left:
                count += 1

            if right:
                count += 1
            
            if count == 2:
                self.found = True

            if (left and right) or node in (p, q):
                return node

            return left or right
        ans = DFS(root)

        return ans if self.found else None
