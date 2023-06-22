from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        leftMinDepth = self.minDepth(root.left)
        if not root.right:
            return leftMinDepth + 1
        rightMinDepth = self.minDepth(root.right)
        if not root.left:
            return rightMinDepth + 1

        return min(leftMinDepth, rightMinDepth) + 1


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
