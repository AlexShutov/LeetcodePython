from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        fringe = [root]
        result = []
        while fringe:
            node = fringe.pop()
            result.append(node.val)
            if node.right:
                fringe.append(node.right)
            if node.left:
                fringe.append(node.left)

        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorderTraversalRecursive(root, result)
        return result

    def preorderTraversalRecursive(self, root: Optional[TreeNode], result):
        if not root:
            return
        result.append(root.val)
        self.preorderTraversalRecursive(root.left, result)
        self.preorderTraversalRecursive(root.right, result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
