"""Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree."""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(val, node):
            if not node:
                return 0

            if val <= node.val:
                output = 1
            else:
                output = 0
            val = max(val, node.val)
            output += dfs(val, node.left)
            output += dfs(val, node.right)

            return output

        return dfs(root.val, root)
