from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        sum = 0
        fringe = [root]
        while fringe:
            currentNode = fringe.pop()
            value = currentNode.val
            if low <= value <= high:
                sum += value
            if currentNode.left:
                fringe.append(currentNode.left)
            if currentNode.right:
                fringe.append(currentNode.right)
        return sum


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
