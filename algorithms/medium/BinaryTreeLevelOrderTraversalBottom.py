from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def reverse(self, items: list[list[int]]):
        l = 0
        r = len(items) - 1
        while l < r:
            items[l], items[r] = items[r], items[l]
            l += 1
            r -= 1

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        self.reverse(levels)
        return levels


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
