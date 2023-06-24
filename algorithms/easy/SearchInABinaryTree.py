from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def searchBSTIterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if val < node.val:
                if node.left:
                    stack.append(node.left)
            elif node.right:
                stack.append(node.right)
        return None


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
