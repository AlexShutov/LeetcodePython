from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        newLeft = None
        newRight = None
        if root.left:
            newLeft = self.invertTree(root.left)
        if root.right:
            newRight = self.invertTree(root.right)
        root.left = newRight
        root.right = newLeft
        return root


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
