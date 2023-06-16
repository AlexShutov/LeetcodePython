from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetricRecursive(self, left: TreeNode, right: TreeNode):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isSymmetricRecursive(left.left, right.right) and self.isSymmetricRecursive(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.isSymmetricRecursive(root.left, root.right)


def getTestData():
    return []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()



