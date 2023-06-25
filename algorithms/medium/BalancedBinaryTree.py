from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root: Optional[TreeNode]):
            if not root:
                return True, 0
            leftBalanced, leftHeight = helper(root.left)
            rightBalanced, rightHeight = helper(root.right)

            if not leftBalanced or not rightBalanced:
                return False, -1
            return abs(leftHeight - rightHeight) < 2, max(leftHeight, rightHeight) + 1

        return helper(root)[0]


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
