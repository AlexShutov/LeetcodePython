from typing import List

def getTestData():
    return [
        (5, 4),
        (1, 1)
    ]

class Solution:

    def __init__(self):
        self.badVersion = 0
        self.versions = 0

    def isBadVersion(self, version: int):
        return version == 4

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            if self.isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    solution = Solution()
    for versions, badVersion in getTestData():
        solution.badVersion = badVersion
        print("For versions " + str(solution.versions) + " first bad version is: " + str(solution.firstBadVersion(versions)))

