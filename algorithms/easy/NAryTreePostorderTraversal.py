from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result

        def helper(currentNode: Node, values: List[int]):
            for child in currentNode.children:
                helper(child, values)
            values.append(currentNode.val)

        helper(root, result)
        return result


def getTestData():
    return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
