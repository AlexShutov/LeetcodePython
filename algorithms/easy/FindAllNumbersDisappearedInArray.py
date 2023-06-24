from typing import List


def getTestData():
    return [
        [4, 3, 2, 7, 8, 2, 3, 1],
        [1, 1]
    ]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsSet = set(nums)
        disappeared = []
        for i in range(1, n + 1):
            if not i in numsSet:
                disappeared.append(i)

        return disappeared


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array in getTestData():
        disappearedNumbers = solution.findDisappearedNumbers(array)
        print("all numbers disappeared from array " + str(array) + " is " + str(disappearedNumbers))
