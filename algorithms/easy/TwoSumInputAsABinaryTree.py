from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        history = set()
        return self.findTargerRecursive(root, history, k)

    def findTargerRecursive(self, root: Optional[TreeNode], history: set, sum) -> bool:
        if not root:
            return False
        target = sum - root.val
        if target in history:
            return True
        history.add(root.val)
        return self.findTargerRecursive(root.left, history, sum) or self.findTargerRecursive(root.right, history, sum)

    def findTargetIterative(self, root: Optional[TreeNode], k: int) -> bool:
        fringe = [root]
        history = set()
        while fringe:
            currentNode = fringe.pop()
            diff = k - currentNode.val
            if diff in history:
                return True
            history.add(currentNode.val)
            if currentNode.left:
                fringe.append(currentNode.left)
            if currentNode.right:
                fringe.append(currentNode.right)
        return False


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
