from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthRecursiveFirst(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        maxDepth = 0
        if root.left:
            maxDepth = self.maxDepth(root.left)
        if root.right:
            maxDepth = max(maxDepth, self.maxDepth(root.right))
        return maxDepth + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfsDepth(root, 0)

    def dfsDepth(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        return max(self.dfsDepth(root.left, depth + 1), self.dfsDepth(root.right, depth + 1))

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, currDepth = queue.popleft()
            if node.left:
                queue.append((node.left, currDepth + 1))
            if node.right:
                queue.append((node.right, currDepth + 1))
            if not queue:
                return currDepth


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
