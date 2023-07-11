"""Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order."""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        output = []

        parent = {}

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    parent[node.left.val] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right.val] = node
                    queue.append(node.right)

        visited = {}
        queue.append(target)

        while k > 0 and queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                visited[node.val] = 1010

                if node.left and node.left.val not in visited:
                    queue.append(node.left)

                if node.right and node.right.val not in visited:
                    queue.append(node.right)

                if node.val in parent and parent[node.val].val not in visited:
                    queue.append(parent[node.val])

            k -= 1

        while queue:
            output.append(queue.popleft().val)

        return output
