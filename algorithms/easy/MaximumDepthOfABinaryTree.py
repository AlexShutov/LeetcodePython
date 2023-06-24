from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
