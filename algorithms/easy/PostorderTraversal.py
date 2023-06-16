from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def helper(head: Optional[TreeNode], result: []):
            if head is None:
                return
            if head.left:
                helper(head.left, result)
            if head.right:
                helper(head.right, result)
            result.append(head.val)

        helper(root, order)
        return order

    def postorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        callStack = [root]
        while callStack:
            currNode = callStack.pop()
            if currNode.left:
                callStack.append(currNode.left)
            if currNode.right:
                callStack.append(currNode.right)
            order.append(currNode.val)

        return order



def getTestData():
    return []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()



