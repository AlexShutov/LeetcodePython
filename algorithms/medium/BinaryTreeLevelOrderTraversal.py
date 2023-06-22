from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = [[root.val]]
        treeFringe = deque([root])
        levelFringe = deque()

        while treeFringe:
            node = treeFringe.popleft()
            if node.left:
                levelFringe.append(node.left)
            if node.right:
                levelFringe.append(node.right)

            if not treeFringe:
                if levelFringe:
                    levels.append([node.val for node in levelFringe])
                    treeFringe = levelFringe
                    levelFringe = deque()
        return levels


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
