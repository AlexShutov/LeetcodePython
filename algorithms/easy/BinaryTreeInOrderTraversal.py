from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverseRecursive(self, root: Optional[TreeNode], result: List[int]):
        if not root:
            return
        self.traverseRecursive(root.left, result)
        result.append(root.val)
        self.traverseRecursive(root.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverseRecursive(root, result)
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
