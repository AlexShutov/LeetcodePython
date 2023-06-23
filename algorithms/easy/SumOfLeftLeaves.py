from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        stack = [(root, None)]
        while stack:
            currNode, isLeft = stack.pop()
            if self.isLeaf(currNode) and isLeft:
                sum += currNode.val
            if currNode.left:
                stack.append((currNode.left, True))
            if currNode.right:
                stack.append((currNode.right, False))

        return sum

    def sumOfLeftLeavesRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and self.isLeaf(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def isLeaf(self, root: Optional[TreeNode]):
        return not root.left and not root.right


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
