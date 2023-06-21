from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        for i in range(len(nums) + 1):
            if i not in numSet:
                return i
        return -1


def getTestData():
    return [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1]
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for numbers in getTestData():
        firstMissingNumber = solution.missingNumber(numbers)
        print("First missing number from range array " + str(numbers) + " is: " + str(firstMissingNumber))
