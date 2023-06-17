"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = collections.deque([root])

        while q:
            rightnode = None
            lenq = len(q)

            for i in range(lenq):
                node = q.popleft()

                if node:
                    rightnode = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightnode:
                output.append(rightnode.val)


        return output
